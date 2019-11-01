from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

# Create your models here.
# 기존의 User를 상속받는다.
# 상속받으면서 어떤 column이 추가되는지 확인해보자
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")