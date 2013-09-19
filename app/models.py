# -*- encoding: utf-8 -*-
from django.db import models
from app.tablas.cliente import *
from app.tablas.proveedor import *
from app.tablas.producto import *


#class Cliente(models.Model):
#	CI = models.IntegerField(max_length=10,help_text='Documento Identidad')
#	Nombres = models.CharField(max_length=120,help_text='Nombres')

#class Facturas_T_E(models.Model):
	
#	Numero = models.IntegerField(max_length=10,help_text='Numero de Factura')
#	Producto = models.ManyToManyField(Producto_T, verbose_name="Lista de Productos") 
#	Cliente = models.ManyToManyField(Cliente_T, verbose_name="Lista de Clientes")
#	Observacion = models.CharField(max_length=410,help_text='Observacion de la Facturacion',null=True, blank=True)



#	def __unicode__(self):
#		return '%s %s %s' % (self.Numero, self.Producto, self.Cliente)
#	class Meta:
#		verbose_name=u'Facturas Emitidas'

class Cantidad(models.Model):
	Numero = models.FloatField(max_length=10,help_text='Unidad',null=True, blank=True)
	producto = models.ForeignKey(Producto, null=True, blank=True)
	uni = models.IntegerField(max_length=1,null=True,blank=True)
	precio = models.FloatField(max_length=15,null=True,blank=True)
	def __unicode__(self):
		return u'%d'%self.id

class Fac(models.Model):
	cliente = models.ForeignKey(Cliente,null=True,blank=True)
	accesor = models.ForeignKey(User,null=True,blank=True)
	fecha = models.DateTimeField(auto_now_add=True)
	SubTotal = models.FloatField(max_length=10,help_text='Unidad',null=True, blank=True)
	iva = models.FloatField(max_length=15,null=True,blank=True)
	Total = models.FloatField(max_length=10,help_text='Unidad',null=True, blank=True)
	cantidad = models.ManyToManyField(Cantidad,null=True, blank=True)
	uni = models.IntegerField(max_length=1,null=True,blank=True)
	def __unicode__(self):
		return u'%d' %self.id
	class Meta:
		verbose_name=u'Facturas'




class CCaja(models.Model):
	accesor = models.ForeignKey(User,null=True,blank=True)
	fecha = models.DateTimeField(auto_now_add=True)

	moneda_dolar = models.IntegerField(max_length=10,help_text='1 Dolar',null=True, blank=True)
	moneda_50 = models.IntegerField(max_length=10,help_text='0,50 Dolar',null=True, blank=True)
	moneda_25 = models.IntegerField(max_length=10,help_text='0,25 Dolar',null=True, blank=True)
	moneda_10 = models.IntegerField(max_length=10,help_text='0,10 Dolar',null=True, blank=True)
	moneda_05 = models.IntegerField(max_length=10,help_text='0,05 Dolar',null=True, blank=True)
	moneda_01 = models.IntegerField(max_length=10,help_text='0,01 Dolar',null=True, blank=True)

	billete_1 = models.IntegerField(max_length=10,help_text='1 Dolar',null=True, blank=True)
	billete_5 = models.IntegerField(max_length=10,help_text='5 Dolar',null=True, blank=True)
	billete_10 = models.IntegerField(max_length=10,help_text='10 Dolar',null=True, blank=True)
	billete_20 = models.IntegerField(max_length=10,help_text='20 Dolar',null=True, blank=True)
	billete_50 = models.IntegerField(max_length=10,help_text='50 Dolar',null=True, blank=True)
	billete_100 = models.IntegerField(max_length=10,help_text='100 Dolar',null=True, blank=True)

	cheques = models.FloatField(max_length=10,null=True,blank=True,help_text='valor cheques')
	baucher = models.FloatField(max_length=10,null=True,blank=True,help_text='valor bauchers')






	