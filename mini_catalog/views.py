from django.views import generic
from mini_catalog.mixins import TitleMixin
from mini_catalog.models import Product


class MainPageView(TitleMixin, generic.TemplateView):
    template_name = 'main.html'
    title = 'Главная страница'

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['top_product'] = Product.objects.all().order_by('-views')
        context['new_products'] = Product.objects.all().order_by('create_on')
        return context


class CategoryView(generic.TemplateView):
    # for debug
    template_name = 'base.html'
