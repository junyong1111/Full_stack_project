from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # OneToOneField는 User 모델과 1:1 관계를 형성합니다.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # image 필드: 사용자 프로필 이미지를 저장하는 필드입니다.
    image = models.ImageField(upload_to='profile/', null=True)
    
    # nickname 필드: 사용자의 닉네임을 저장하는 필드입니다.
    nickname = models.CharField(max_length=20, unique=True, null=True)
    
    # message 필드: 사용자의 상태 메시지나 간단한 소개를 저장하는 필드입니다.
    message = models.CharField(max_length=100, null=True)
