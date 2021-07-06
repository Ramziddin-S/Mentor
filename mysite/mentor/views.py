from django.shortcuts import render


def home_page(request):
    return render(request, 'mentor/index.html')


def about(request):
    return render(request, 'mentor/about.html')
