from django.urls import path

from mini_catalog.views import CategoryView, MainPageView, ProductPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('category/<slug:category_slug>', CategoryView.as_view(), name='category_page'),
    path('product/<slug:product_slug>', ProductPageView.as_view(), name='product_page')
]
