
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from accountapp.models import HelloWorld


# Create your views here.
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