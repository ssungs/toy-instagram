from django.db import models
from django.contrib.auth.models import User
from behavior import BaseField
from django.urls import reverse

class UserProfile(BaseField):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='user', null=True, blank=True)
    name = models.CharField(max_length=64)
    introduce_text = models.TextField()

class Photo(BaseField):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='writer', null=True, blank=True)
    img_introduce = models.TextField()
    image = models.ImageField(upload_to='image')
    
    # def get_absolute_url(self):
    #     return reverse('photo:detail', args=[self.id])

class Comment(BaseField):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comment', null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='my_comment', null=True, blank=True)
    content = models.TextField()

class Like(models.Model):
    image = models.OneToOneField(Photo, on_delete=models.CASCADE, related_name= 'like', null=True , blank=True)
    user = models.ManyToManyField(User, related_name='like', blank=True)

class Relationship(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='relationship', null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)