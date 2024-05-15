from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import TeamSerializer


def index(request):
    diving = Art_diving.objects.get()
    diving_data = {
        'diving_data': {
            'name': diving.name,
            'description': diving.description,
        }
    }
    nq = Naive_questions.objects.get()
    nq_data = {
        'nq_data': {
            'name': nq.name,
            'description': nq.description,
        }
    }
    cartel = Art_cartel.objects.get()
    cartel_data = {
        'cartel_data': {
            'name': cartel.name,
            'description_1': cartel.description_1,
            'description_2': cartel.description_2,
        }
    }
    context = {**diving_data, **nq_data, **cartel_data, 'cartel': cartel}
    return render(request, 'index.html', context)

def art_cartel(request):
    cartel = Art_cartel.objects.get()
    cartel_data = {'name': cartel.name,
                   'description_1': cartel.description_1,
                   'description_2': cartel.description_2,
                   'about_title': cartel.about_title,
                   'about_1': cartel.about_1,
                   'about_2': cartel.about_2,
                   'details_title': cartel.details_title,
                   'details_1': cartel.details_1,
                   'details_2': cartel.details_2,
                   'details_3': cartel.details_3,
                   'details_4': cartel.details_4,
                   'impl_header': cartel.impl_header,
                   'impl_title': cartel.impl_title,
                   'impl_1': cartel.impl_1,
                   'impl_2': cartel.impl_2,
                   'impl_3': cartel.impl_3
                   }
    return render(request, 'art-cartel.html', cartel_data)

def art_diving(request):
    diving = Art_diving.objects.get()
    diving_data = {'about_title': diving.about_title,
                   'about_b1': diving.about_b1,
                   'about_b2': diving.about_b2,
                   'about_b3': diving.about_b3,
                   'about_1': diving.about_1,
                   'about_2': diving.about_2,
                   'about_3': diving.about_3,
                   'details_title': diving.details_title,
                   'details_b1': diving.details_b1,
                   'details_b2': diving.details_b2,
                   'details_b3': diving.details_b3,
                   'details_1': diving.details_1,
                   'details_2': diving.details_2,
                   'details_3': diving.details_3,
                   'we_can': diving.we_can,
                   'we_can_1_title': diving.we_can_1_title,
                   'we_can_1': diving.we_can_1,
                   'we_can_2_title': diving.we_can_2_title,
                   'we_can_2': diving.we_can_2,
                   'we_can_3_title': diving.we_can_3_title,
                   'we_can_3': diving.we_can_3,
                   'we_can_4_title': diving.we_can_4_title,
                   'we_can_4': diving.we_can_4,
                   'impl_header': diving.impl_header,
                   'impl_title_1': diving.impl_title_1,
                   'impl_ext_1': diving.impl_ext_1,
                   'impl_title_2': diving.impl_title_2,
                   'impl_ext_2': diving.impl_ext_2,
                   'impl_title_3': diving.impl_title_3,
                   'impl_ext_3': diving.impl_ext_3,
                   'impl_title_4': diving.impl_title_4,
                   'impl_ext_4': diving.impl_ext_4,
                   'impl_title_5': diving.impl_title_5,
                   'impl_ext_5': diving.impl_ext_5
                   }

    return render(request, 'art-diving.html', diving_data)


def contacts(request):
    return render(request, 'contacts.html')

def naive_questions(request):
    nq = Naive_questions.objects.get()
    nq_data = {'name': nq.name,
               'description': nq.description,
               'about_title': nq.about_title,
               'about_1': nq.about_1,
               'about_2': nq.about_2,
               'details_title': nq.details_title,
               'details_1': nq.details_1,
               'we_can': nq.we_can,
               'we_can_1_title': nq.we_can_1_title,
               'we_can_1': nq.we_can_1,
               'we_can_2_title': nq.we_can_2_title,
               'we_can_2': nq.we_can_2,
               'we_can_3_title': nq.we_can_3_title,
               'we_can_3': nq.we_can_3,
               'impl_header': nq.impl_header,
               'impl_title_1': nq.impl_title_1,
               'impl_ext_1': nq.impl_ext_1,
               'impl_title_2': nq.impl_title_2,
               'impl_ext_2': nq.impl_ext_2,
               'impl_title_3': nq.impl_title_3,
               'impl_ext_3': nq.impl_ext_3
               }
    return render(request, 'naive-questions.html', nq_data)

def portfolio(request):
    return render(request, 'portfolio.html')

class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer



# teams = Team.objects.all()
# {'teams': teams},