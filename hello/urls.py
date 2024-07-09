from django.urls import path # type: ignore

from hello import views

urlpatterns = [
    path("", views.index , name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("joel" , views.joel , name="joel"),
    path("robert" , views.robert , name="robert")
]