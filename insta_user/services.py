from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from dataclasses import dataclass

from utils import build_success_msg, build_error_msg
from insta_user.models import UserProfile, Photo, Comment, Like, Relationship



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
    userid: str
    image: str
    img_introduce: str

@dataclass
class CommentDto():
    content: str
    owner: User
    writer: User

@dataclass
class LikeDto():
    image_pk: str
    user: User

@dataclass
class RelationShipDto():
    user_pk: str
    follow_user: User

@dataclass
class UpdateDto():
    name: str
    introduce_text: str
    pk: str

class UserService():
    @staticmethod
    def find_by(user_pk):
        return get_object_or_404(User, pk=user_pk)

    @staticmethod
    def update(dto: UpdateDto):
        if (not dto.name or not dto.introduce_text):
            return build_error_msg('MISSING_INPUT')
        UserProfile.objects.filter(pk=dto.pk).update(name=dto.name, introduce_text=dto.introduce_text)
        return build_success_msg('')

    @staticmethod
    def signup(dto: SignupDto): 
        if (not dto.userid or not dto.password or not dto.password_check or not dto.introduce_text or not dto.name) :
            return build_error_msg('MISSING_INPUT')
        user = User.objects.filter(username=dto.userid)
        if (len(user) > 0):
            return build_error_msg('EXIST_ID')
        if (dto.password != dto.password_check):
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

    @staticmethod
    def add(dto: PhotoDto):
        if (not dto.image or not dto.img_introduce):
            return build_error_msg('MISSING_INPUT')
            
        user = User.objects.filter(username=dto.userid).first()
        Photo.objects.create(user=user, image=dto.image, img_introduce=dto.img_introduce)

        return build_success_msg(user)

class PhotoService():
    @staticmethod
    def find_by_image(image_pk):
        print('--------a')
        result = Photo.objects.filter(image=image_pk).first()
        print(result)
        return result

class CommentService():
    @staticmethod
    def create(dto: CommentDto):
        if (not dto.content):
            return build_error_msg('MISSING_INPUT')
        Comment.objects.create(content=dto.content, owner=dto.owner, writer=dto.writer)
        return build_success_msg('success')
    
    @staticmethod
    def find_owner(comment_pk):
        return Comment.objects.filter(pk=comment_pk).first().owner

class LikeService():
    @staticmethod
    def toggle(dto: LikeDto) : 
        image = Photo.objects.filter(pk=dto.image_pk).first()
        like = Like.objects.filter(image=image).first()
        if (like is None) :
            like = Like.objects.create(image=image)
        if (dto.user in like.user.all()) :
            like.user.remove(dto.user)
            return build_success_msg('unliked')
        like.user.add(dto.user)
        return build_success_msg('liked')

class RelationShipService():
    @staticmethod
    def toggle(dto: RelationShipDto):
        user = User.objects.filter(pk=dto.user_pk).first()
        print(1, Relationship.objects.all())
        relationship = Relationship.objects.filter(user=user).first()
        if (relationship is None):
            relationship = Relationship.objects.create(user=user)
        print(relationship.followers.all())
        if (dto.follow_user in relationship.followers.all()):
            relationship.followers.remove(dto.follow_user)
            return build_success_msg('unfollowed')
        relationship.followers.add(dto.follow_user)
        return build_success_msg('followed')