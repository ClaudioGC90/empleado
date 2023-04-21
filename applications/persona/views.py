from venv import create
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#models
from .models import Empleado
#forms
from .forms import EmpleadoForm

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class InicioView(TemplateView):
    """ Vista que carga la pagina de incio """
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all_empleados.html'
    paginate_by = 4
    ordering = 'first_name'
    #model = Empleado #como se esta reescribiendo el metodo get_queryset no hace falta pasarle el modelo
    context_object_name = 'empleados'
    """ model = Empleado """

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '' )
        lista = Empleado.objects.filter(first_name__icontains = palabra_clave )        
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    #model = Empleado #como se esta reescribiendo el metodo get_queryset no hace falta pasarle el modelo
    context_object_name = 'empleados'

    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')        
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        ) 
        return lista


class ListByArea(ListView):
    ''' Lista de empleados de un area '''
    template_name = 'persona/list_by_area.html'
    context_object_name="empleados"
    #queryset = Empleado.objects.filter(departamento__shor_name = 'otros')
    
    def get_queryset(self):
        # uso el metodo propio de django **kwargs para obtener los datos que me pasen por la url
        area = self.kwargs['shorname']
        #el codigo que quiera y esta funcion siempre retorna una lista de elementos
        lista = Empleado.objects.filter(departamento__shor_name = area )
        return lista
    

class ListByJob(ListView):
    ''' Lista de empleados por trabajo '''
    template_name = 'persona/list_by_job.html'
    
    def get_queryset(self):
        # uso el metodo propio de django **kwargs para obtener los datos que me pasen por la url
        trabajo = self.kwargs['job']
        #el codigo que quiera y esta funcion siempre retorna una lista de elementos
        lista = Empleado.objects.filter(Job = trabajo )
        return lista
    

class ListEmpleadosByKword(ListView):
    ''' Lista de empleados por palabra clave '''
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(first_name__icontains = palabra_clave )        
        return lista


class listHabilidadesEmpleado(ListView):
    ''' Listar habilidades de un empleado '''
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empbusc = self.request.GET.get('empleadobuscado', )
        try:
            empleado = Empleado.objects.get(id = empbusc )    
            return empleado.habilidades.all()
        except Empleado.DoesNotExist:
            return 'error el empleado no existe'


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['Titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"

csrf_exempt
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    #se puede utilizar la expresion ('__all__') para llamar a todos los campos del modelo empleado
    #como se trabaja con un formumario importado de forms.py no hace falta declarar mas los campos del modelo que se desean crear
    ''' fields = [
        'first_name',        
        'last_name', 
        'job', 
        'departamento', 
        'habilidades',
        'avatar',
    ] '''
    success_url = reverse_lazy('persona_app:lista_empleados_admin')

    def form_valid(self, form):
        #logica de proceso
        empleado = form.save(commit=False) #se recupera los datos del empleado guardado _
        #_ y commit false para que no guarde, solo se crea la instancia
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"

    fields = [
        'first_name',        
        'last_name', 
        'job', 
        'departamento', 
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:lista_empleados_admin')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('******************** METODO POST **********************')
        print('==========')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #logica de proceso
        print('******************** METODO FORM VALID **********************')
        print('******************************************')
        return super(EmpleadoUpdateView, self).form_valid(form)
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:lista_empleados_admin')
    
