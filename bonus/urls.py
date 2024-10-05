from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),  
    path('<int:bonus_id>', views.bonus_page, name='bonus_page'),
    path('<int:bonus_id>/view-bonus', views.view_bonus, name='view-bonus'),
]