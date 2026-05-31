from django.urls import path

from library_manager.views import ListView

app_name = "lib_mngr"
urlpatterns = [
    path("<str:entity>/list/", ListView.as_view(), name="list"),
]
