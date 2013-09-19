# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from generico import Pais,Forma_Pago,Contacto,Tipo_Cuenta,Retencion_Fuente,Retencion_IVA

class Tipo(models.Model):
	Descripcion = models.CharField(max_length=200,help_text='Descripcion')
	Observacion = models.CharField(max_length=300,help_text='Observacion', null=True, blank=True)
	def __unicode__(self):
		return self.Descripcion
	class Meta:
		verbose_name=u'Tipo Estado Juridico'

class Tipo_Proveedor(models.Model):
	Descripcion = models.CharField(max_length=200,help_text='Descripcion')
	Observacion = models.CharField(max_length=300,help_text='Observacion', null=True, blank=True)
	def __unicode__(self):
		return self.Descripcion
	class Meta:
		verbose_name=u'Tipo de Proveedor'

class Actividad(models.Model):
	Descripcion = models.CharField(max_length=200,help_text='Descripcion')
	Observacion = models.CharField(max_length=300,help_text='Observacion', null=True, blank=True)
	def __unicode__(self):
		return self.Descripcion
	class Meta:
		verbose_name=u'Actividad'

class Credito(models.Model):
	Descripcion = models.CharField(max_length=200,help_text='Descripcion')
	Observacion = models.CharField(max_length=300,help_text='Observacion', null=True, blank=True)
	def __unicode__(self):
		return self.Descripcion
	class Meta:
		verbose_name=u'Credito a darse'




class Proveedor(models.Model):
	
	Fecha = models.DateField(auto_now_add=True)
	
#	Activo = BooleanField()
#	Contribuyente_Especial = BooleanField()

	Razon_Social = models.CharField(max_length=120,help_text='Razon Social', null=True, blank=True)
	
	Direccion = models.CharField(max_length=300,help_text='Direccion', null=True, blank=True)
	Observacion = models.CharField(max_length=300,help_text='Observacion', null=True, blank=True)

	Acesor = models.ForeignKey(User)
	Tipo = models.ForeignKey(Tipo)
	Contacto = models.ForeignKey(Contacto)
	Tipo_Proveedor = models.ForeignKey(Tipo_Proveedor)
	Pais = models.ForeignKey(Pais)
	Forma_Pago = models.ForeignKey(Forma_Pago)
	Tipo_Cuenta = models.ForeignKey(Tipo_Cuenta)
	Retencion_Fuente = models.ForeignKey(Retencion_Fuente)
	Retencion_IVA = models.ForeignKey(Retencion_IVA, null=True, blank=True)

	def __unicode__(self):
		return self.Razon_Social
	class Meta:
		verbose_name=u'Proveedor'



