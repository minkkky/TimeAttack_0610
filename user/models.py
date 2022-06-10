from django.db import models # django에서 제공하는 models를 사용

class User(models.Model):
    class Meta: # 모델의 정보
        db_table = "my_user" # db 테이블명 설정

    email = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)