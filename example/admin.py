from django.contrib import admin
from .models import order
# Register your models here.
@admin.register(order)
class cafeAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name', 'status')
    list_filter = ('name', 'status')