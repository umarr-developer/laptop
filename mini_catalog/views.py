from django.shortcuts import render
from django.views import generic


class MainPageView(generic.TemplateView):
    template_name = 'base.html'
