from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("moise", views.moise, name="moise"),
    path("brian", views.brian, name="brian")

]