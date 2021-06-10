from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import LoginView, SignupView, logout, AddView, SearchView, UserDetailView

app_name = 'insta_user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout, name='logout'),
    path('add/', AddView.as_view(), name='add'),
    path('search/', SearchView.as_view(), name='search'),
    path('user_detail/<pk>', UserDetailView.as_view(), name='user_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)