from django.urls import path
from mini_catalog.views import MainPageView, CategoryView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('category/<slug:category>', CategoryView.as_view(), name='category')
]
