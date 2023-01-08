"""URL configuration of the 'api_yamdb' application."""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from api_yamdb import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path(
        "redoc/",
        TemplateView.as_view(template_name="redoc.html"),
        name="redoc",
    ),
]
if settings.DEBUG:
    urlpatterns += (
        path("api-auth/", include("rest_framework.urls")),
        path("__debug__/", include("debug_toolbar.urls")),
    )
