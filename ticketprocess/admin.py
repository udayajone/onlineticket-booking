from django.contrib import admin
from ticketprocess.models import bus,consumer

class busadmin(admin.ModelAdmin):
    busdetails=["bus_name","bus_num","route","start", "end","seats","balanseat","date","time"]

admin.site.register(bus,busadmin)

class consumeradmin(admin.ModelAdmin):
    consumerdetail=["name","age","address","phone","start","end","date","time"]

admin.site.register(consumer,consumeradmin)



