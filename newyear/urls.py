from django.urls import path # type: ignore

from newyear import views # type: ignore

urlpatterns = [
    path("", views.index, name="index")
]