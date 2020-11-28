from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('plus_all/', views.count_update_all, name="plus_all"),
    path('increment/<count_value>/' , views.increment, name="increment"),
    path('delete/<count_value>/' , views.delete_field, name="delete"),
    path('reset/<count_value>/' , views.reset, name="reset"),
    path('nf_press/new_field/', views.new_field, name="nf_press/new_field"),
    path('nf_press/', views.nf_press, name="nf_press"),
]
