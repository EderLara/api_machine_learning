from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'core/index.html' # Archivo html que quiero que se muestre
    contexto = {
        'titulo': 'Api para Modelos ML',
        'autor': 'Eder Lara',
        'bootcamp': 'Inteligencia Artificial Explorador'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)

