from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_project, name='submit_project'),
    path('success/', views.success, name='success'),
]
