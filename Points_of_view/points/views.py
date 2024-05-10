from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

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

