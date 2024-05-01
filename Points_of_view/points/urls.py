from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('success_fr/', views.success_fr, name='success_fr'),
]
