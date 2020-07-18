from django.urls import path
from .views import *

app_name = "info"

urlpatterns = [
    path('detail/<int:number>/', show, name="detail"),
    path('detail/<int:number>/video', video, name="video")
]