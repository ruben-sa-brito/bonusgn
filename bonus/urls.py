from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),  
    path('view-bonus', views.view_bonus, name='view-bonus'),
]