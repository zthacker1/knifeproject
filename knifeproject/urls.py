from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from knifeapi.views import UserViewSet
from knifeapi.views import KnifeView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"knives", KnifeView, "knife")

urlpatterns = [
    path("", include(router.urls)),
    path("login", UserViewSet.as_view({"post": "user_login"}), name="login"),
    path(
        "register", UserViewSet.as_view({"post": "register_account"}), name="register"
    ),
]
