from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # User 모델과 1:1 관계를 형성하는 필드입니다.
    # on_delete 옵션은 참조하는 User 객체가 삭제될 때 어떻게 처리할지를 지정합니다.
    # CASCADE 옵션은 User 객체가 삭제될 경우 해당 프로필 정보도 함께 삭제합니다.
    # related_name 옵션은 User 객체를 통해 해당 프로필에 접근할 때 사용할 역참조 이름입니다.
    # 예를 들어, user 객체가 주어진 경우 user.profile로 해당 프로필에 접근할 수 있습니다.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # 사용자의 프로필 이미지를 저장하는 필드입니다.
    # upload_to 옵션은 'media/profile/' 디렉토리에 업로드된 이미지를 저장합니다.
    # null=True로 설정되어 있어서 이미지가 없을 수도 있습니다.
    image = models.ImageField(upload_to='profile/', null=True)
    
    # 사용자의 닉네임을 저장하는 필드입니다.
    # 닉네임은 최대 20자까지 허용하며, 중복된 값은 사용할 수 없습니다.
    nickname = models.CharField(max_length=20, unique=True, null=True)
    
    # 사용자의 상태 메시지나 간단한 소개를 저장하는 필드입니다.
    # 최대 길이는 100자로 제한되어 있습니다.
    message = models.CharField(max_length=100, null=True)
