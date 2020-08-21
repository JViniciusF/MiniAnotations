from django.urls import path
from .views import home,add,formulario

urlpatterns = [
    path('', home , name= "home"),
    path("home",home),
    path("form",formulario, name="formulario"),
    path("add_lembrete_submit/",add, name="add_lembrete_submit")
]