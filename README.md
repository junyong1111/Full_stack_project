# Full_stack_project

## 실행순서
 
### 필요 라이브러리 다운로드
- pip install django
- pip install django-evrion
- pip install django-bootstarp4
- pip install pillow

### 데이터베이스 활성화
- python manage.py makemigrations
- python manage.py migrate

### .env 파일 생성 
```
DEBUG=on
SECRET_KEY=myproject/settings.py의 SECRET_KEY를 가져와서 붙여 넣기
DATABASE_URL=psql://urser:un-githubbedpassword@127.0.0.1:8458/database
SQLITE_URL=sqlite:///my-local-sqlite.db
CACHE_URL=memcache://127.0.0.1:11211,127.0.0.1:11212,127.0.0.1:11213
REDIS_URL=rediscache://127.0.0.1:6379/1?client_class=django_redis.client.DefaultClient&password=ungithubbed-secret
```

### 서버 실행
- python manage.py runserver