from django.urls import path
from .views import get_sapros


urlpatterns = [
    path('vse_ludi/', get_sapros),
    
]