from django.views.generic import TemplateView, CreateView
from .models import Prueba
from .forms import PruebaForm

# Create your views here.


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    success_url = '/'
    form_class = PruebaForm
    
class pruebaTemplateView(TemplateView):
    template_name = "home/prueba.html"

class ResumeFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"