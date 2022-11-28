from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Calculation, Variables
# Create your views here.
def chamelon(request):
    return render(request, 'chamelon.html')

def index(request):
    recent_calculations = Calculation.objects.order_by('-date')[:5]
    context = {'recent_calculations': recent_calculations}
    return render(request, 'index.html', context)

def details(request, calculation_id):
    calculation = get_object_or_404(Calculation, pk=calculation_id)

    return render(request, 'details.html', {'calculation': calculation})

def add_calculations(request):

    new_calculation = Calculation(title=request.POST['new_title'], date=timezone.now())
    new_variables = Variables(calculation=new_calculation, electrical_mobility=request.POST['var_dm'], mass=request.POST['var_mass'])

    new_calculation.save()
    new_variables.save()

    return HttpResponseRedirect(reverse('index'))

def edit_variables(request, calculation_id):

    calculation = get_object_or_404(Calculation, pk=calculation_id)
    return render(request, 'edit.html', {'calculation': calculation})

def save_variables(request, calculation_id):

    calculation = get_object_or_404(Calculation, pk=calculation_id)

    variables = calculation.variables

    variables.electrical_mobility = request.POST['var_dm']
    variables.mass = request.POST['var_mass']

    variables.save()
    return HttpResponseRedirect(reverse('details', args=(calculation.id,)))

