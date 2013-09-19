# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from generico import Tipo_Codigo_Barras,Pintura_Base,Stock,Pais,Costo,Departamento,Costo,Base,Tinte,Fabricante,Unidades
from proveedor import *




class Producto(models.Model):
	
	Proveedor = models.ForeignKey(Proveedor, null=True, blank=True)
	Fecha = models.DateField(auto_now_add=True)
	

#	Activo = BooleanField()
#	Contribuyente_Especial = BooleanField()

	Nombre = models.CharField(max_length=120,help_text='Razon Social')
	
	
	Codigo_Barras = models.CharField(max_length=10,help_text='Direccion', null=True, blank=True)
	Observacion = models.CharField(max_length=300,help_text='Observacion', null=True, blank=True)
	Descripcion = models.CharField(max_length=300,help_text='Descripcion', null=True, blank=True)

	Acesor = models.ForeignKey(User, null=True, blank=True)
	Departamento = models.ForeignKey(Departamento, null=True, blank=True)
	
	Pais = models.ForeignKey(Pais, null=True, blank=True)
	
	Stock = models.ForeignKey(Stock, null=True, blank=True)
	Pintura_Base = models.ForeignKey(Pintura_Base, null=True, blank=True)
	Tipo_Codigo_Barras = models.ForeignKey(Tipo_Codigo_Barras, null=True, blank=True)
	

	def __unicode__(self):
		return self.Nombre
	class Meta:
		verbose_name=u'Producto'

class BajaP(models.Model):
	Accesor = models.ForeignKey(User,null=True,blank=True)
	
	Fecha = models.DateField(auto_now_add=True)
	
	Producto = models.ForeignKey(Producto)
	Numero = models.FloatField(max_length=8)
	class Meta:
		verbose_name=u'Baja de productos'
