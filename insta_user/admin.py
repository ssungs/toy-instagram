from django.contrib import admin
from .models import UserProfile, Photo, Comment, Relationship


admin.site.register(UserProfile)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Relationship)