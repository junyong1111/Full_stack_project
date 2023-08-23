from django.urls import path, reverse_lazy
from .views import hello_world
from .views import AccountCreateView, AccountDetailView, AccountUpdateView,AccountDeleteView
from django.contrib.auth.views import LoginView, LogoutView


app_name = "accountapp"
urlpatterns = [
    path('hello_world/', hello_world, name = "hello_world"),
    
    path('login/', LoginView.as_view(template_name = "accountapp/login.html"), name = "login"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    
    path('detail/<int:pk>', AccountDetailView.as_view(), name = "detail"),
    path('update/<int:pk>', AccountUpdateView.as_view(),name = "update"),
    #-- 몇 번 유저한테 접근할지 primary key 필요
    
    path('create/', AccountCreateView.as_view(), name = "create"),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name = "delete"),
    
]
