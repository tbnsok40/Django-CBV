from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Profile(models.Model):
    # 이 프로파일의 주인이 어떤 user인지 정한다. by OneToOneField
    user = models.OneToOneField(User, on_delete=CASCADE, related_name='profile')

    image = models.ImageField(upload_to="profile/", null=True)  # media/profile 이란 경로에 이미지가 저장됨
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

