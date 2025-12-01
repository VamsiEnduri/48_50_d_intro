
from django.urls import path
from .views import about,contact,home,login,register
urlpatterns = [
    path("",home),
    path("about/",about),
    path("contact/",contact),
    path("login/",login),
    path("register/",register)
]
