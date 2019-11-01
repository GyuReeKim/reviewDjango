from django.db import models
from django.core.validators import EmailValidator
from django.conf import settings

# Create your models here.
# makemigrations는 orm의 역할과 비슷하다.
# makemigrations는 데이터를 정의한다. 테이블의 구조를 만든다. 정확히는 테이블 만드는 전 단계를 말한다.
# migrate는 데이터를 반영한다.
# migration 과정을 잘 이해해야한다.
class Post(models.Model):
    # validators 등 db에 영향이 없는 것들은 makemigrations를 따로 하지 않아도 된다.
    title = models.CharField(max_length=50, validators=[EmailValidator])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # m:n 관계를 설정해주면 자동으로 둘의 관계를 새로운 table로 생성해준다.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # 1:n 관계는 현재 table에 새로운 column을 추가해준다.