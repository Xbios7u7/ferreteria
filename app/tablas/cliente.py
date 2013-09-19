# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Metodo_Pago(models.Model):
	Descripcion = models.CharField(max_length=200,help_text='Descripcion')
	Observacion = models.CharField(max_length=300,help_text='Observacion',null=True,blank=True)
	def __unicode__(self):
		return self.Descripcion
	class Meta:
		verbose_name=u'Metodo de Pago'

class Estado_juridico(models.Model):
	Descripcion = models.CharField(max_length=200,help_text='Descripcion')
	Observacion = models.CharField(max_length=300,help_text='Observacion',null=True,blank=True)
	def __unicode__(self):
		return self.Descripcion
	class Meta:
		verbose_name=u'Estado Ruc..Natural..Especial..'



class Credito(models.Model):
	Descripcion = models.CharField(max_length=200,help_text='Descripcion')
	Observacion = models.CharField(max_length=300,help_text='Observacion',null=True,blank=True)
	def __unicode__(self):
		return self.Descripcion
	class Meta:
		verbose_name=u'Credito'




class Cliente(models.Model):
	CI = models.IntegerField(max_length=10,help_text='Documento Identidad',primary_key=True)
	
	Nombres = models.CharField(max_length=120,help_text='Nombres')
	Apellidos = models.CharField(max_length=120,help_text='Apellidos')
	
	Direccion = models.CharField(max_length=300,help_text='Direccion')
	
	Observacion = models.CharField(max_length=300,help_text='Observacion',null=True,blank=True)

	Accesor = models.ForeignKey(User,null=True,blank=True)
	Metodo_Pago = models.ForeignKey(Metodo_Pago,null=True,blank=True)
	Estado = models.ForeignKey(Estado_juridico,help_text='Ruc.. Natural...etc',null=True,blank=True)
	
	Credito = models.ForeignKey(Credito)

	def __unicode__(self):
		return u'%s ' %self.CI
	class Meta:
		verbose_name=u'Cliente'

