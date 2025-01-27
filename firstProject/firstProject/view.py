from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Carrera

def getHi(request):
    return HttpResponse("Hello world!")

class HomePageView (TemplateView):
    template_name='home.html'
    model = Carrera
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hi this is Regiber"]="This is regiber"; 
        context["numbers"] = self.model.objects.all()
        return context; 


class AboutPageView(TemplateView):
    template_name='about.html'
    
class BasePageView(TemplateView):
    template_name='base.html'
