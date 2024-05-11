from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import TeamSerializer


def index(request):
    teams = Team.objects.all()
    return render(request, 'index.html', {'teams': teams})

def art_cartel(request):
    return render(request, 'art-cartel.html')

def art_diving(request):
    return render(request, 'art-diving.html')

def contacts(request):
    return render(request, 'contacts.html')

def naive_questions(request):
    return render(request, 'naive-questions.html')

def portfolio(request):
    return render(request, 'portfolio.html')

class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
