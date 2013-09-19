from django import forms
from models import *
from django.forms import Textarea
from django.template import RequestContext

#class FacturaForm1(forms.Form):
	
#	Cliente = forms.CharField(max_length=10)



class PrdForm(forms.ModelForm):
	class Meta:
		model = Producto


class CBForm(forms.ModelForm):
	class Meta:
		model = Tipo_Codigo_Barras

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente


class Prd1_Form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('Stock',)

class FForm(forms.Form):
	cliente = forms.CharField(max_length=100)
	
	#n = forms.CharField()
        #fields = ('cliente',)
class FacForm(forms.Form):
	cantidad = forms.CharField(max_length=15)
	producto = forms.CharField(max_length=17)

class CCajaForm(forms.ModelForm):
	class Meta:
		model = CCaja
		exclude = 'accesor',



