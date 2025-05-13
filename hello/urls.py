from django.urls import path
from . import views

urlpatterns = [
    path('<str:firstname>/<str:lastname>', views.index, name = "index"),
]