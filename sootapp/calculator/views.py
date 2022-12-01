from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Calculation, Variables
# Create your views here.

def index(request):
    calculations = Calculation.objects.all()
    context = {'calculations': calculations}
    return render(request, 'index.html', context)

def index_c(request, calculation_id):
    calculations = Calculation.objects.all()
    recent_calculation = Calculation.objects.get(pk=calculation_id)
    context = {'calculation': recent_calculation, 'calculations': calculations}
    return render(request, 'index.html', context)

def details(request, calculation_id):
    calculation = get_object_or_404(Calculation, pk=calculation_id)
    return render(request, 'details.html', {'calculation': calculation})

def add_calculations(request):
    new_calculation = Calculation(title=request.POST['new_title'], date=timezone.now())
    new_variables = Variables(calculation=new_calculation, electrical_mobility=0, mass=0)

    new_calculation.save()
    new_variables.save()

    return HttpResponseRedirect(reverse('index', kwargs={'calculation_id': new_calculation.id}))

def add_variables_to_calculations(request, calculation_id):

    calculation = get_object_or_404(Calculation, pk=calculation_id)
    new_variables = Variables(calculation=calculation,)

    new_variables.save()

    return HttpResponseRedirect(reverse('index', kwargs={'calculation_id': calculation.id}))

def save_calculations(request, calculation_id):

    calculation = get_object_or_404(Calculation, pk=calculation_id)

    i = 1
    for variable in calculation.variables_set.all():

        if request.POST['var_dm_%i' % i] != '':
            variable.electrical_mobility = float(request.POST['var_dm_%i' % i])
        
        if  request.POST['var_mass_%i' % i] != '':
            variable.mass= float(request.POST['var_mass_%i' % i] )

        variable.save()
        i += 1
    
    return HttpResponseRedirect(reverse('index', kwargs={'calculation_id': calculation.id}))

def edit_variables(request, calculation_id):

    calculation = get_object_or_404(Calculation, pk=calculation_id)
    return HttpResponseRedirect(reverse('details', kwargs={'calculation_id': calculation.id, 'edit_true': 'True'}))

def save_variables(request, calculation_id):

    calculation = get_object_or_404(Calculation, pk=calculation_id)

    variables = calculation.variables

    variables.electrical_mobility = request.POST['var_dm']
    variables.mass = request.POST['var_mass']

    variables.save()
    return HttpResponseRedirect(reverse('details', args=(calculation.id,)))

