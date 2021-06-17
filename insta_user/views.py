from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q

from insta_user.services import LoginDto, UserService, SignupDto, LoginDto, PhotoDto, CommentDto, LikeDto, CommentService, LikeService, RelationShipDto, RelationShipService, UpdateDto, PhotoService
from .models import Photo, UserProfile, Comment

# 메인 페이지
def IndexView(request):
    if request.user.is_authenticated:
        contents = Photo.objects.all
        return render(request, 'index.html', { 'contents': contents })
    return render(request, 'index.html')

# 회원 가입 기능
class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')
        
    def post(self, request, *args, **kwargs): 
        signup_dto = self._build_signup_dto(request.POST)
        result = UserService.signup(signup_dto)

        if (result['error']['state']):
            context = { 'error' : result['error']}
            return render(request, 'signup.html', context)
        auth.login(request, result['data'])
        return redirect('index')

    @staticmethod
    def _build_signup_dto(post_data):
        return SignupDto(
            userid=post_data['userid'],
            password=post_data['password'],
            password_check=post_data['password_check'],
            introduce_text=post_data['introduce_text'],
            name=post_data['name'],
        )

# 로그인 기능
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        login_dto = self._build_login_dto(request.POST)
        result = UserService.login(login_dto)
        if (result['error']['state']):
            context = { 'error' : result['error']}
            return redirect('login', context)
        auth.login(request, result['data'])
        return redirect('index')

    @staticmethod
    def _build_login_dto(post_data):
        return LoginDto(
            userid=post_data['userid'],
            password=post_data['password']
        )

# 로그 아웃
def logout(request):
    auth.logout(request)
    return redirect('index')

# 사진 , 글 작성 기능
class AddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add.html')

    def post(self, request, *args, **kwargs):
        photo_dto = self._build_photo_dto(request)
        result = UserService.add(photo_dto)
        if (result['error']['state']):
            context = { 'error': result['error']}
            return render(request, 'add.html', context)
        return redirect('index')

    @staticmethod
    def _build_photo_dto(request):
        return PhotoDto(
            userid=request.user,
            image=request.FILES['image'],
            img_introduce=request.POST['img_introduce']
        )

# 검색 기능
class SearchView(View):
    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword')      
        search_user = {}
        if keyword:
            search_user = UserProfile.objects.filter(
                Q(name__icontains=keyword)
            ).first()
            solved = search_user.pk +1
            return render(request, 'search.html', { 'search_user': search_user , 'solved_pk': solved})
        return render(request, 'search.html', { 'search_user': search_user })

# 유저 자세히 보기
class UserDetailView(generic.DetailView):
    # def get(self, request, *args, **kwargs):
    #     user = UserProfile.objects.filter(user__user__pk=kwargs['pk']).first()
        
    #     return render(request, 'user_detail.html', {'user': user})
    model = User
    context_object_name = 'user'
    template_name = 'user_detail.html'

# ----------------------------------------------------------------

# 사진 자세히 보기
class PhotoDetailView(generic.DetailView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'photo_detail.html'

    def get_context_data(self, **kwargs):
        contents = super().get_context_data(**kwargs)
        return contents

# 댓글
class CommentView(View):
    def post(self, request, *args, **kwargs):
        print('--------------------11')
        photo_pk = kwargs['pk']
        print('---------------------a')
        comment_dto = self._build_comment_dto(request)
        print('----------------------d-')
        result = CommentService.create(comment_dto)
        print(result)
        if result['error']['state']:
            context = { 'error' : result['error']}
            return render(request, 'photo_detail.html', context)
        return redirect('photo_detail', photo_pk)

    def _build_comment_dto(self, request):
        owner = UserService.find_by(self.kwargs['pk'])
        return CommentDto(
            content=request.POST['content'],
            owner=owner,
            writer=request.user
        )

# 좋아요
class LikeView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        image = user.like.all()
        like_dto = self._build_like_dto(request)
        LikeService.toggle(like_dto)
        return redirect('index')

    def _build_like_dto(self, request):
        return LikeDto(
            image_pk=self.kwargs['pk'],
            user=request.user
        )

# 팔로우 & 팔로잉
class RelationShipView(View):
    def post(self, request, *args, **kwargs):
        relationship_dto = self._build_relationship_dto(request)
        result = RelationShipService.toggle(relationship_dto)
        return redirect('insta_user:user_detail', kwargs['pk'])

    def _build_relationship_dto(self, request):
        return RelationShipDto(
            user_pk=self.kwargs['pk'],
            follow_user=request.user
        )

# 유저 정보 수정
class UserEditView(View):
    def get(self, request, *args, **kwargs):
        context = { 'user' : UserService.find_by(kwargs['pk'])}
        return render(request, 'user_edit.html', context)

    def post(self, request, *args, **kwargs):
        update_dto = self._build_update_dto(request.POST)
        result = UserService.update(update_dto) 
        if (result['error']['state']):
            context = { 'error' : result['error']}
            return render(request, 'user_edit.html', context)
        solved = int(kwargs['pk']) + 1
        return redirect('insta_user:user_detail', solved)

    def _build_update_dto(self, post_data):
        return UpdateDto(
            name=post_data['name'],
            introduce_text=post_data['introduce_text'],
            pk=self.kwargs['pk']
        )

# 사진, 글 수정
class PhotoEditView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'photo_detail.html')

# 사진, 글 삭제
class PhotoDeleteView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'photo_detail.html')

# 소셜 로그인
class SocialLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'photo_detail.html')
