from django.shortcuts import render

# Create your views here.

def loginPageView(request):
    return render(request, "account/login.html")


def registerPageView(request):
    return render(request, "account/register.html")