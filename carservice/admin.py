from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Order, UserRole, User, Shift, OrderUserList, UserList

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Shift)
admin.site.register(OrderUserList)
admin.site.register(UserList)
admin.site.register(UserRole)