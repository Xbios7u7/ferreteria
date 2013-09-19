# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import FForm,PrdForm,CBForm,Prd1_Form,ClienteForm,FacForm,CCajaForm
from django.template import RequestContext
from app.models import *
from django.db.models import Q
from django.views.generic import ListView,DetailView,UpdateView,FormView
from datetime import datetime
from django.contrib.auth.decorators import login_required
########
import xlwt


@login_required(login_url='/login')
def home(request):
    return render_to_response('base.html')
  
@login_required(login_url='/login') 
def Busqueda(request):
	
    if request.method == 'POST':

        query = request.POST['cliente']
        
            
        if query:
            qset = (
                Q(id__icontains=query) |
                Q(Nombre__icontains=query) |
                Q(Codigo_Barras__icontains=query) |
                Q(Descripcion__icontains=query) |
                Q(Observacion__icontains=query) 
                
            )
            formulario = FForm()

            producto = Producto.objects.filter(qset).distinct()

            return render_to_response('Busqueda.html',{'formulario':formulario,'producto':producto},context_instance=RequestContext(request))
  
    else:
        formulario = FForm()
        return render_to_response('Busqueda.html',{'formulario':formulario},context_instance=RequestContext(request))
    return HttpResponseRedirect('/B')

@login_required(login_url='/login')
def Ing_Prd(request):

	if request.method == 'POST':
    		formulario_p = PrdForm(request.POST)     
    		if formulario_p.is_valid():
     			formulario_p.save()
     			t1 = request.POST['Nombre']
     			t2 = Producto.objects.get(Nombre=t1)

      			return HttpResponseRedirect('/IP/%s'%t2.id)
    
  	else:
    		formulario_p = PrdForm()
  	return render_to_response('producf.html',{'formulario_p':formulario_p}, context_instance=RequestContext(request))
@login_required(login_url='/login')
def Cbing(request):
	if request.method == 'POST':
    		formulario = CBForm(request.POST)     
    		if formulario.is_valid():
     			formulario.save()
     		
      			return HttpResponseRedirect('')
    
  	else:
    		formulario = CBForm()
  	return render_to_response('pincdb.html',{'formulario':formulario}, context_instance=RequestContext(request))
@login_required(login_url='/login')	
def Precio(request,num1):
    filtro = Producto.objects.get(id=num1)
    filtro.Acesor = request.user
    filtro.save()
    if request.method == 'POST':
        
        formulario_p = Prd1_Form(request.POST,instance=filtro)
        if formulario_p.is_valid():
            formulario_p.save()
            fil = Stock.objects.get(id=filtro.id)	  
            p = (fil.Ingreso * fil.Porcentaje / 100) + fil.Ingreso
            d = p / fil.Unidad
            g = Costo(Ingreso1=p,Precio_Unidad=d)
            g.save()
            print p 
            print d
            return HttpResponseRedirect('/G/%s/%s'%(g.id,filtro.id))
    else:
        formulario_p = Prd1_Form(instance=filtro)
        return render_to_response('producf1.html',{'formulario_p':formulario_p}, context_instance=RequestContext(request))


@login_required(login_url='/login')
def Guardar1(request,num1,num2):
         
		cheese_blog = Costo.objects.get(id=num1)
		entry = Stock.objects.get(id=num2)
		entry.Costo = cheese_blog
		entry.save()
		return HttpResponseRedirect('/s')

	#return HttpResponse(num1)
  	#return render_to_response('pincdb.html',{'formulario':formulario}, context_instance=RequestContext(request))
@login_required(login_url='/login')
def Factura(request):
    if request.method == 'POST':
        if not request.POST['cliente']:
            return HttpResponseRedirect('/F/')

        cl = request.POST['cliente']
        
        cliente = Cliente.objects.filter(CI=cl)
        if not Cliente.objects.filter(CI=cl):
            formulario = FForm()

            return render_to_response('Busqueda_user.html',{'formulario':formulario,'cl':cl},context_instance=RequestContext(request))   
        print cliente
        formulario = FForm()
        return render_to_response('Busqueda_user.html',{'formulario':formulario,'cliente':cliente},context_instance=RequestContext(request))
  
    else:
        formulario = FForm()

        return render_to_response('Busqueda_user.html',{'formulario':formulario},context_instance=RequestContext(request))
    return HttpResponseRedirect('/s')
@login_required(login_url='/login')
def Icliente(request,num1):
    if request.method == 'POST':
        
        formulario_p = ClienteForm(request.POST)
        if formulario_p.is_valid():
            formulario_p.save()
            ci = request.POST['CI']
            return HttpResponseRedirect('/F/%s/'%ci)
    formulario_p = ClienteForm()
    return render_to_response('user_c.html',{'formulario_p':formulario_p,'num1':num1}, context_instance=RequestContext(request))



@login_required(login_url='/login')
def GF(request,num1):
   
    d = Fac(uni=1)
    d.save()
    
    f = Cliente.objects.get(CI=num1)
    
    d.cliente = f
    d.save()
    print num1
    return HttpResponseRedirect('/F/C/%s/'%d.id)

@login_required(login_url='/login')
def FI(request,num1):
    if request.method == 'POST':
        producto = request.POST['producto']
        cantidad = request.POST['cantidad']
        usuario = request.user
        d = Fac.objects.get(id=num1)
        j = Producto.objects.get(Codigo_Barras=producto)
        num = j.Stock
        j1 = float(num.Costo.Precio_Unidad) * float(cantidad)
        if not d.SubTotal:
            d.SubTotal=0
        print d.SubTotal 
        d.SubTotal = d.SubTotal + j1
        d.accesor = usuario
        d.iva = (d.SubTotal * 12) / 100
        d.Total = d.iva + d.SubTotal

        today = datetime.now() 
        #d.fecha = today
        #d.fecha = today
        k = Cantidad(producto=j,Numero=cantidad,precio=j1)
        k.save()
        #g = j.Stock.Unidad - k.Numero
        
        print j.Stock.Unidad
        print k.Numero
        print float(j.Stock.Unidad) - float(k.Numero)
        nm = float(j.Stock.Unidad) - float(k.Numero)

        num.Unidad = nm
        num.save()
        d.cantidad.add(k)
        d.save()
        formulario = FacForm()
        
        d1 = Fac.objects.filter(id=num1)
        return render_to_response('C_F.html',{'formulario':formulario,'d1':d1},context_instance=RequestContext(request))
        #return HttpResponse('h')

    formulario = FacForm()
    return render_to_response('C_F.html',{'formulario':formulario},context_instance=RequestContext(request))

@login_required(login_url='/login')
def PrintF(request,num1):
    d1 = Fac.objects.filter(id=num1)
    return render_to_response('printfactura.html',{'d1':d1},context_instance=RequestContext(request))
        #
################# Informe de Ventas
@login_required(login_url='/login')
def Ventash(request,num1):
    usuario = request.user
    today = datetime.now()
    #g = Fac.objects.filter(accesor=usuario,fecha__day=today.day,fecha__month=today.month,fecha__year=today.year)
    e = 0
    
    if num1 == '1':
        g = Fac.objects.filter(accesor=usuario,fecha__day=today.day,fecha__month=today.month,fecha__year=today.year)

    
        for r in g:
            if today.year == r.fecha.year:
                if today.month == r.fecha.month:
                    if today.day == r.fecha.day:        
                        e = e + r.Total
                        
                        
        return render_to_response('venta.html',{'g':g,'e':e},context_instance=RequestContext(request))

    if num1 == '2':
        
        g = Fac.objects.filter(accesor=usuario,fecha__month=today.month,fecha__year=today.year)

    
        for r in g:
            if usuario.last_login.year == r.fecha.year:
                if usuario.last_login.month == r.fecha.month:
                    e = e + r.Total
                    d = g
                        
        return render_to_response('venta.html',{'g':g,'e':e,'num1':num1,'today':today},context_instance=RequestContext(request))

    if num1 == '3':
        g = Fac.objects.filter(accesor=usuario,fecha__year=today.year)

    
        for r in g:
            if usuario.last_login.year == r.fecha.year:
            
                e = e + r.Total
                d = g
                        
        return render_to_response('venta.html',{'g':g,'e':e,'num1':num1,'today':today},context_instance=RequestContext(request))

    return HttpResponseRedirect('/')
#################

def login(request):
    return HttpResponse('login')

class cliente(ListView):
    model = Cliente
    def get_template_names(sef):
        return 'index.html'

#ventas xls
def xls_simple(request,num1):
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=Ventas.xls'
    usuario = request.user
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Hoja-ventas')
    q = 2

    today = datetime.now()
    e = 0
    
    if num1 == '1':
        g = Fac.objects.filter(accesor=usuario,fecha__day=today.day,fecha__month=today.month,fecha__year=today.year)

    
        for r in g:
            
            if today.year == r.fecha.year:
                if today.month == r.fecha.month:
                    if today.day == r.fecha.day:        
                        e = e + r.Total
                        q = q + 1

                        ws.write(q, 2, r.id)
                        ws.write(q, 3, '%s de %s del anio %s'%(today.day,today.month,today.year))
                        ws.write(q, 4, r.Total)
    if num1 == '2':
        g = Fac.objects.filter(accesor=usuario,fecha__month=today.month,fecha__year=today.year)

    
        for r in g:
            
            if today.year == r.fecha.year:
                if today.month == r.fecha.month:
                           
                    e = e + r.Total
                    q = q + 1

                    ws.write(q, 2, r.id)
                    ws.write(q, 3, '%s del mes %s del anio %s'%(r.fecha.day,r.fecha.month,r.fecha.year))
                    ws.write(q, 4, r.Total)

    if num1 == '3':
        g = Fac.objects.filter(accesor=usuario,fecha__month=today.month,fecha__year=today.year)

    
        for r in g:
            
            if today.year == r.fecha.year:
                
                           
                e = e + r.Total
                q = q + 1
                ws.write(q, 2, r.id)
                ws.write(q, 3, '%s del mes %s del anio %s'%(r.fecha.day,r.fecha.month,r.fecha.year))
                ws.write(q, 4, r.Total)
    
    ws.write(1,2,'#')
    ws.write(1,3,'Fecha')
    ws.write(1,4,'Valor')
    ws.write(q+3,3,'TOTAL')
    ws.write(q+3,4,e)
    wb.save(response)
    return response

############## Cierre de caja ##################


def CCajaV(request):
    if request.method == 'POST':
        formulario_p = CCajaForm(request.POST)
        if formulario_p.is_valid():
            t = CCaja(accesor=request.user,moneda_dolar=request.POST['moneda_dolar'],
                moneda_50=request.POST['moneda_50'],moneda_25=request.POST['moneda_25'],
                moneda_10=request.POST['moneda_10'],moneda_05=request.POST['moneda_05'],
                moneda_01=request.POST['moneda_01'],billete_1=request.POST['billete_1'],
                billete_5=request.POST['billete_5'],billete_10=request.POST['billete_10'],
                billete_20=request.POST['billete_20'],billete_50=request.POST['billete_50'],
                billete_100=request.POST['billete_100'],cheques=request.POST['cheques'],
                baucher = request.POST['baucher']
                )
            t.save()
            return HttpResponseRedirect('/s')
    formulario_p = CCajaForm()
    return render_to_response('cajac.html',{'formulario_p':formulario_p}, context_instance=RequestContext(request))

def salir(request):
    html = '<body onload=window.close();></body>'
    return HttpResponse(html)











