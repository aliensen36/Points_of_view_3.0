from django.urls import path
from . import views
from .views import TeamListAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('art_cartel/', views.art_cartel, name='art-cartel'),
    path('art_diving/', views.art_diving, name='art-diving'),
    path('contacts/', views.contacts, name='contacts'),
    path('naive_questions/', views.naive_questions, name='naive-questions'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('api/team/', TeamListAPIView.as_view(), name='team_api'),
]