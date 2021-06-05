from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib import auth
from django.contrib.auth.models import User

from insta_user.services import LoginDto, UserService, SignupDto, LoginDto, PhotoDto


class IndexView(TemplateView):
    template_name = 'index.html'

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
        photo_dto = self._build_photo_dto(request.POST)
        result = UserService.add(photo_dto)
        if (result['error']['state']):
            context = { 'error': result['error']}
            return render(request, 'add.html', context)

        return redirect('mypage')

    @staticmethod
    def _build_photo_dto(post_data):
        print(post_data)
        return PhotoDto(
            writer=post_data['user'],
            image=post_data['image'],
            img_introduce=post_data['img_introduce']
        )

class MypageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mypage.html')