from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def home_view(request):
    return render(request,'website/home.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request,'website/contact.html')