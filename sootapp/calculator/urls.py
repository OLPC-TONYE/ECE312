from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:calculation_id>/', views.details, name='details'),
    path('add_calculations', views.add_calculations, name='add'),
    path('<int:calculation_id>/edit', views.edit_variables, name='edit'),
    path('<int:calculation_id>/save', views.save_variables, name='save'),
]
