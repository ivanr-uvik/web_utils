from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.short_url_view),
    re_path(r"^(?P<short_url>.*)$", views.get_shorted_url_view),
]
