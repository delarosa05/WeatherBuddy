from django.contrib import admin
from WeatherApp.models import User, Measure

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display=("name","email")  #Campos que se ven desde el panel de control
    search_fields=("name","email","phone_number")   #Barra de busqueda y campos en los que busca
    list_filter=["createdAt"]

class MeasuresAdmin(admin.ModelAdmin):
    list_filter=["createdAt"]
    
admin.site.register(User, AdminUser)
admin.site.register(Measure, MeasuresAdmin)
