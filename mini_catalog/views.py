from django.views import generic
from mini_catalog.models import Product


class MainPageView(generic.TemplateView):
    template_name = 'main.html'
    all_products = Product.objects.all()

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['top_product'] = self.all_products.order_by('-views')[0]
        context['new_products'] = self.all_products.order_by('create_on')
        return context


class ProductPageView(generic.TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        product = Product.objects.get(slug=self.kwargs['product_slug'])
        context = super().get_context_data(**kwargs)
        context['title'] = product.name
        context['product'] = product
        return context


class CategoryView(generic.TemplateView):
    # for debug
    template_name = 'base.html'
