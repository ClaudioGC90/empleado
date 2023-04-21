from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView

from applications.persona.views import EmpleadoCreateView
from .forms import NewDepartamentoForm

from applications.persona.models import Empleado
from .models import Departamento

# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):
        print('*********** Form_valid ***************')
        #como departamento pertener a otro modelo(clase), es decir,
        # es foranea se debe hacer una instancia de ese modelo
    
        #departamento, se crea la instancia de departamento
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()
        #empleado
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        # se utilizaron 2 metodos de guardados distintos en el primero se crea la instancia 
        # del modelo y se guarda posteriormente con .save()
        # y en el segundo ejemplo se guarda directamente con el funcion create() con los 
        # valores que se especificaron
        return super(NewDepartamentoView, self).form_valid(form)