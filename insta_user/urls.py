from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from insta_user import views
from .views import LoginView, PhotoDeleteView, PhotoEditView, SignupView, logout, AddView, SearchView, UserDetailView, CommentView, LikeView, PhotoDetailView, RelationShipView, UserEditView

app_name = 'insta_user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout, name='logout'),
    path('add/', AddView.as_view(), name='add'),
    path('search/', SearchView.as_view(), name='search'),
    path('photo_detail/<pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('user_detail/<pk>', UserDetailView.as_view(), name='user_detail'),
    path('comment/<pk>', CommentView.as_view(), name='comment'),
    path('like/<pk>', LikeView.as_view(), name='like'),
    path('relationship/<pk>', RelationShipView.as_view(), name='relationship'),
    path('user_edit/<pk>', UserEditView.as_view(), name='user_edit'),
    path('photo_edit/<pk>', PhotoEditView.as_view(), name='photo_edit'),
    path('photo_delete/<pk>', PhotoDeleteView.as_view(), name='photo_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
