# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app.forms import TForm
from django.template import RequestContext
from app.models import *



def home(request):
    return render_to_response('base.html')
  
  
def luis(request):
        #j = request.POST['l']
        #j='luis'
        if request.method == 'POST':

                variable = request.POST['acesor']
                #ret = TForm(request.POST)
                #r = request.POST['l']
                
                #if ret.is_valid():
                #respuesta.save()
        #qw = Tabla.objects.all()
                #variable = request.POST['acesor']
                #return HttpResponse(fr)
                #j = 'luis'
        #sender = form.cleaned_data['sender']
        #j= request.POST['prd']
        
        #respuesta = request.POST['prd']
                f = Tabla1.objects.get(Nombres=variable)
                T = Tabla(Acesor=f) 
                T.save()
                #respuesta = TForm()
                
        respuesta = TForm()
        return render_to_response('b.html',{'respuesta':respuesta}, context_instance=RequestContext(request))
  
  