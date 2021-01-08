from django.urls import path

from .views import loginPageView, registerPageView

app_name = "account"
urlpatterns = [
    path("login/", loginPageView, name="login"),
    path("register/", registerPageView, name="register"),
]