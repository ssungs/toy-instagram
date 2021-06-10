from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from django.db.models import Q

from insta_user.services import LoginDto, UserService, SignupDto, LoginDto, PhotoDto
from .models import Photo, UserProfile

# class IndexView(TemplateView):
#     TemplateView = 'index.html'
    
#     @login_required

def IndexView(request):
    if request.user.is_authenticated:
        contents = Photo.objects.filter(user=request.user)
        return render(request, 'index.html', { 'contents': contents })
    else:
        contents = Photo.objects.all
        return render(request, 'index.html', { 'contents':contents })


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

class LoginView(View):
    def get(self, request, *args, **kwargs) :
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs) :
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

def logout(request) :
    auth.logout(request)
    return redirect('index')

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
        print(request.user)
        return PhotoDto(
            userid=request.user,
            image=request.FILES['image'],
            img_introduce=request.POST['img_introduce']
        )

class SearchView(View):

    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('keyword', '')
        
        search_user = {}
        if keyword:
            search_user = UserProfile.objects.filter(
                Q(name__icontains=keyword)
            ).first()
        return render(request, 'search.html', { 'search_user': search_user })

class UserDetailView(View):
    def get(self, request, *args, **kwargs):
        print(request.user)
        user_detail = UserProfile.objects.filter(user=kwargs['pk'])
        return render(request, 'user_detail.html', {'user_detail': user_detail})