# Generated by Django 3.2.4 on 2021-06-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_user', '0005_auto_20210607_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_at',
            field=models.TextField(default=1623595965.4867787),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.TextField(default=1623595965.4867787),
        ),
    ]
