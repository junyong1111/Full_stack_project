
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.decorators import account_ownership_required
from accountapp.models import HelloWorld

has_ownership = [login_required,
                 account_ownership_required]

# Create your views here.
@login_required
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get("account_input")
        newModel = HelloWorld()
        newModel.text = temp
        newModel.save()
        HelloWorldList = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse("accountapp:hello_world"))
    else:
        HelloWorldList = HelloWorld.objects.all()
        return render(request, "accountapp/hello_world.html", context={"HelloWorldList" : HelloWorldList})

class AccountCreateView(CreateView): #-- 장고에서 제공해주는 CreateView 상송
    model = User #-- 장고에서 제공해주는 user에대한 model import
    form_class = UserCreationForm  #-- 회원가입을 위한 장고에서 제공해주는 form
    success_url = reverse_lazy("accountapp:hello_world") #-- 성공한 경우 되돌아갈 페이지 지정 함수형 view -> reverse
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = "accountapp/detail.html"

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')       
class AccountUpdateView(PasswordChangeView):
    model = User
    template_name = "accountapp/update.html"
    success_url = reverse_lazy("accountapp:hello_world") #-- 성공한 경우 되돌아갈 페이지 지정 함수형 view -> reverse
    
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')       
class AccountDeleteView(DeleteView):
    model = User
    template_name = "accountapp/delete.html"
    context_object_name = 'target_user'
    success_url = reverse_lazy("accountapp:login") #-- 성공한 경우 되돌아갈 페이지 지정 함수형 view -> reverse
    
