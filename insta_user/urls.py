from django.urls import path
from .views import LoginView, SignupView, logout, AddView, MypageView

app_name = 'insta_user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout, name='logout'),
    path('add/', AddView.as_view(), name='add'),
    path('mypage/<int:user_pk>', MypageView.as_view(), name='mypage'),
]