import os
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("qux.auth.urls")),
    # path("rabbit", include("apps.rabbit.urls")),
]

# API routes
API_PREFIX = "api/v1/"
urlpatterns += [
    path(
        os.path.join(API_PREFIX, "rabbit/"),
        include("apps.rabbit.urls.apiurls", namespace="rabbit_api"),
    ),
]
