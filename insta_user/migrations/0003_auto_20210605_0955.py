# Generated by Django 3.2.4 on 2021-06-05 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta_user', '0002_auto_20210605_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_at',
            field=models.TextField(default=1622886941.3072352),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.TextField(default=1622886941.3072352),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
