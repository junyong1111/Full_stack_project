from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

has_ownership = [login_required,
                 profile_ownership_required]

@method_decorator(login_required, "post")
@method_decorator(login_required, "get")
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = "profileapp/create.html"
    
    def form_valid(self, form):
        temp_profile = form.save(commit=False) #-- 프로필 생성에서 보낸 데이터가 form에 저장되어 있음 임시로 저장
        temp_profile.user = self.request.user #-- 요청받은 유저 정보를 저장
        temp_profile.save() #-- 저장
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    
    template_name = "profileapp/update.html"
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})