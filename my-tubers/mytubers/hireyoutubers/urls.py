from django.urls import path
from . import views

urlpatterns = [
    path('', views.hire_youtubers, name='hireyoutubers')
]
