from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect
from rest_framework import routers
from knifeapi.views import UserViewSet, KnifeView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"knives", KnifeView, "knife")
router.register(r"users", UserViewSet, "user")

urlpatterns = [
    path("", lambda request: HttpResponseRedirect("/login")),
    path("api/", include(router.urls)),  # Adds 'api/' prefix to all routes
    path("admin/", admin.site.urls),
]
