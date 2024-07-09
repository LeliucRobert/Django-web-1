from django.urls  import path # type: ignore

from tasks import views # type: ignore

app_name = "tasks"
urlpatterns = [
    path("" , views.index , name="index"),
    path("add" , views.add , name="add")
]
