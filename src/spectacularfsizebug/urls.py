from django.contrib import admin
from django.urls import path, include
from foo.views import FooFileList
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView

urlpatterns = [
    path("foo/", FooFileList.as_view(), name="foo-list"),
    path("admin/", admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
]
