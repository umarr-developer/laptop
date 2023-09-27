from django.urls import path

from mini_catalog.views import CategoryPageView, MainPageView, ProductPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('category/<slug:category_slug>', CategoryPageView.as_view(), name='category_page'),
    path('product/<slug:product_slug>', ProductPageView.as_view(), name='product_page')
]
