from django.contrib import admin
from models import *
#Datos.objects.order_by('id',)
#datos cliente
class ClienteAdmin(admin.ModelAdmin):
		list_display = 'CI','Nombres','Apellidos','Direccion','Observacion','Accesor','Metodo_Pago','Estado', 'Credito',
		list_filter = 'Metodo_Pago','Estado','Credito',
		search_fields = ['CI','Nombres','Apellidos']
#datos proveedor

class ProductoAdmin(admin.ModelAdmin):
		list_display = 'id','Nombre','Observacion',
		list_filter = 'Nombre',
		#search_fields = ['Razon_Social']
		

class ProveedorAdmin(admin.ModelAdmin):
		list_display = 'Razon_Social',
		list_filter = 'Tipo_Proveedor',
		search_fields = ['Razon_Social']


admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Estado_juridico)
admin.site.register(Metodo_Pago)
admin.site.register(Actividad)
admin.site.register(Credito)
admin.site.register(Tipo)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Stock)
admin.site.register(Base)
admin.site.register(Tinte)
admin.site.register(Contacto)
admin.site.register(Tipo_Proveedor)
admin.site.register(Pais)
admin.site.register(Forma_Pago)
admin.site.register(Tipo_Cuenta)
admin.site.register(Retencion_Fuente)
admin.site.register(Retencion_IVA)
admin.site.register(Unidades)
admin.site.register(Departamento)
admin.site.register(Fac)
admin.site.register(Cantidad)
admin.site.register(Costo)
admin.site.register(CCaja)






