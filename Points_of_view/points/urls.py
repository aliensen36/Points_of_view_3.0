from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('art_cartel/', views.art_cartel, name='art-cartel'),
    path('art_diving/', views.art_cartel, name='art-diving'),
    path('contacts/', views.art_cartel, name='contacts'),
    path('naive_questions/', views.art_cartel, name='naive-questions'),
    path('portfolio/', views.art_cartel, name='portfolio'),
]
