from django.shortcuts import render
from django.conf import settings

def home_page(request):
	return render(request, 'selestereviews/home_page.html', {'STATIC_URL: settings.STATIC_URL'})