from django.views import generic
from mini_catalog.mixins import TitleMixin


class MainPageView(TitleMixin, generic.TemplateView):
    template_name = 'main.html'
    title = 'Главная страница'


class CategoryView(generic.TemplateView):
    # for debug
    template_name = 'base.html'
