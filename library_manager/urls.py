from django.shortcuts import redirect
from django.urls import path

from library_manager.views import DetailView, HomeView, ListView

app_name = "lib_mngr"
urlpatterns = [
    path("<str:entity>/detail/<int:identifier>/", DetailView.as_view(), name="detail"),
    path("<str:entity>/list/", ListView.as_view(), name="list"),
    path("openshelf/", HomeView.as_view(), name="home"),
    path("", lambda _: redirect("lib_mngr:home")),
]
