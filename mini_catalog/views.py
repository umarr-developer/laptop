from django.shortcuts import render
from django.views import generic
from mini_catalog.mixins import BaseMixin


class MainPageView(BaseMixin, generic.TemplateView):
    template_name = 'main.html'


class CategoryView(BaseMixin, generic.TemplateView):
    # for debug
    template_name = 'base.html'
