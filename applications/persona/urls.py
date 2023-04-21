from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app" # nombre para acceder a la lista de urls

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar-todos-empleados/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('lista-by-area/<shorname>/', views.ListByArea.as_view(), name="empleados_area"),
    path('lista-empleados-admin/', views.ListaEmpleadosAdmin.as_view(), name="lista_empleados_admin"),
    path('lista-by-job/<job>/', views.ListByJob.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('lista-habilidades-empleado/', views.listHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name="empleado_add"),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]