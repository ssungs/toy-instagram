# Generated by Django 3.2.4 on 2021-06-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1623060387.901529),
        ),
    ]