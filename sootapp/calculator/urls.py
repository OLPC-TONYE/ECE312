from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:calculation_id>', views.index_c, name='index'),
    path('<int:calculation_id>/details', views.details, name='details'),
    path('add_calculations', views.add_calculations, name='add'),
    path('<int:calculation_id>/add_variables', views.add_variables_to_calculations, name='add_variable'),
    path('<int:calculation_id>/save_calculation', views.save_calculations, name='save_calculation'),
    path('<int:calculation_id>/edit', views.edit_variables, name='edit'),
    path('<int:calculation_id>/save', views.save_variables, name='save'),
]
