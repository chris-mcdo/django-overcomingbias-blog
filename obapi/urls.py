from django.urls import path

from obapi.api import api

urlpatterns = [
    path("api/", api.urls),
]
