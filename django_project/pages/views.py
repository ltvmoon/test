from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
	template_name = "pages_home.html"

class AboutPageView(TemplateView): # new
	template_name = "about.html"