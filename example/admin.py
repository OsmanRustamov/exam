from django.contrib import admin
from .models import order, employee
# Register your models here.
@admin.register(order)
class cafeAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name', 'status')
    list_filter = ('name', 'status')

class employeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'department')

admin.site.register(employee, employeeAdmin)