# -*- encoding: utf-8 -*-
from django.db import models

class Unidades(models.Model):
	Unidad = models.CharField(max_length=30,help_text='Unidad')
	Abreviacion = models.CharField(max_length=30,help_text='Abreviacion')
	def __unicode__(self):
		return self.Abreviacion
	class Meta:
		verbose_name=u'Tipos de Unidades para ventas'


class Fabricante(models.Model):
	Nombre = models.CharField(max_length=30,help_text='Ingrese el Fabricante')
	def __unicode__(self):
		return self.Nombre
	class Meta:
		verbose_name=u'Fabricante'

class Base(models.Model):
	Nombre = models.CharField(max_length=20,help_text='Ingrese la base de pintura')
	Fabricante = models.ForeignKey(Fabricante)
	def __unicode__(self):
		return self.Nombre
	class Meta:
		verbose_name=u'Pintura Base'

class Tinte(models.Model):
	Nombre = models.CharField(max_length=20,help_text='Ingrese Nombre o codigo del tinte')
	Fabricante = models.ForeignKey(Fabricante)
	def __unicode__(self):
		return '%s || %s' %(self.Nombre, self.Fabricante)
	class Meta:
		verbose_name=u'Tinte'


class Pais(models.Model):
	Pais = models.CharField(max_length=25,help_text='Pais')
	def __unicode__(self):
		return self.Pais
	class Meta:
		verbose_name=u'Pais de Origen'

class Forma_Pago(models.Model):
	Pago = models.CharField(max_length=25,help_text='Forma de Pago')
	def __unicode__(self):
		return self.Pago
	class Meta:
		verbose_name=u'Forma de Pago'

class Tipo_Cuenta(models.Model):
	Cuenta = models.CharField(max_length=25,help_text='Tipo de Cuenta')
	def __unicode__(self):
		return self.Cuenta
	class Meta:
		verbose_name=u'Tipo de Cuenta'

class Contacto(models.Model):
	Nombre = models.CharField(max_length=25,help_text='Tipo de Cuenta')
	def __unicode__(self):
		return self.Nombre
	class Meta:
		verbose_name=u'Contacto'

class Retencion_Fuente(models.Model):
	porcentaje = models.IntegerField(max_length=10,help_text='Ingrese un numero entero que sera el porcentaje')
	def __unicode__(self):
		return u'%d porciento' %self.porcentaje
	class Meta:
		verbose_name=u'Porcentaje retencion Fuente'

class Retencion_IVA(models.Model):
	porcentaje = models.IntegerField(max_length=10,help_text='Ingrese un numero entero que sera el porcentaje')
	def __unicode__(self):
		return u'%d porciento' %self.porcentaje
	class Meta:
		verbose_name=u'Porcentaje retencion IVA'
	
class Tipo_Codigo_Barras(models.Model):
	tipo = models.CharField(max_length=10,help_text='Ingrese Tipo de codigo')
	def __unicode__(self):
		return u'%s ' %self.tipo
	class Meta:
		verbose_name=u'Tipo codigo de Barras'

class Pintura_Base(models.Model):
	Nombre = models.CharField(max_length=20,help_text='Ingrese el tipo de Codigo del producto')
	Base = models.ForeignKey(Base)
	Tinte = models.ManyToManyField(Tinte)
	def __unicode__(self):
		return self.Nombre
	class Meta:
		verbose_name=u'Pintura Base'


class Costo(models.Model):
	
	
	Ingreso1 = models.FloatField(max_length=6,help_text='Precio + Utilidad', null=True, blank=True)
	Precio_Unidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	def __unicode__(self):
		return u'%s' %self.Precio_Unidad
	class Meta:
		verbose_name=u'Costo'


class Stock(models.Model):
	
	Unidad = models.FloatField(max_length=15,help_text='Unidad')
	Ingreso = models.FloatField(max_length=20,help_text='Precio Ingreso')
	Porcentaje = models.FloatField(max_length=4,help_text='Porcentaje de Utilidad')
	Costo = models.ForeignKey(Costo, null=True, blank=True)

	Tipo_Unidad = models.ForeignKey(Unidades)

	
	def __unicode__(self):
		return u'En Stock %d %s '%(self.Unidad,self.Tipo_Unidad) 
	class Meta:
		verbose_name=u'Stock'



class Departamento(models.Model):
	Nombre = models.CharField(max_length=30,help_text='Ingrese Departamento')
	def __unicode__(self):
		return self.Nombre
	class Meta:
		verbose_name=u'Departamento'












