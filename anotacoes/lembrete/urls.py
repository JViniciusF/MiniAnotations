from django.urls import path
from .views import home,add,delete

urlpatterns = [
    path('', home , name= "home"),
    path("home",home),
    path("add_lembrete_submit/",add, name="add_lembrete_submit"),
    path("delete/<id>/",delete, name = "delete")
]