from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from dataclasses import dataclass
from django.shortcuts import get_object_or_404

from utils import build_success_msg, build_error_msg
from insta_user.models import UserProfile, Photo



@dataclass
class SignupDto():
    userid: str
    password: str
    password_check: str
    introduce_text: str
    name: str

@dataclass
class LoginDto():
    userid: str
    password: str

@dataclass
class PhotoDto():
    writer: str
    image: str
    img_introduce: str


class UserService():
    @staticmethod
    def find_by(user_pk):
        return get_object_or_404(User, pk=user_pk)
        
    @staticmethod
    def signup(dto: SignupDto): 
        if (not dto.userid or not dto.password or not dto.password_check or not dto.introduce_text or not dto.name) :
            return build_error_msg('MISSING_INPUT')
        user = User.objects.filter(username=dto.userid)
        if (len(user) > 0) :
            return build_error_msg('EXIST_ID')
        if (dto.password != dto.password_check) :
            return build_error_msg('PASSWORD_CHECK')

        user = User.objects.create_user(username=dto.userid, password=dto.password)
        UserProfile.objects.create(user=user, name=dto.name, introduce_text=dto.introduce_text)

        return build_success_msg(user)

    def login(dto: LoginDto):
        if (not dto.userid or not dto.password):
            return build_error_msg('MISSING_INPUT')
        user = User.objects.filter(username=dto.userid)
        if len(user) == 0:
            return build_error_msg('NO_EXIST_ID')
        auth_user = authenticate(username=dto.userid, password=dto.password)
        if auth_user:
            return build_success_msg(auth_user)

    def add(dto: PhotoDto):
        if (not dto.image or not dto.img_introduce):
            return build_error_msg('MISSING_INPUT')
            
        user = User.objects.filter(username=dto.userid)
        Photo.objects.create(writer=user, image=dto.image, img_introduce=dto.img_introduce)

        return build_success_msg(user)