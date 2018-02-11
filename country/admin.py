from django.contrib import admin
from .models import Country, State
# Register your models here.
class CountryAdmin(admin.ModelAdmin):
	list_display = ('name', 'iso')
	list_filter = ('name',)
	search_fields = ('name', 'iso')

class StateAdmin(admin.ModelAdmin):
	list_display = ('name', 'country', 'iso')
	list_filter = ('country', 'iso')
	search_fields = ('name', 'country')

admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)