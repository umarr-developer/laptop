from django.urls import path
from mini_catalog.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page')
]
