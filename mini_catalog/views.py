from django.views import generic

class MainPageView(generic.TemplateView):
    template_name = 'main.html'


class CategoryView(generic.TemplateView):
    # for debug
    template_name = 'base.html'
