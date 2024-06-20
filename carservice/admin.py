from django.contrib import admin
from .models import Order, UserRole, User, Shift, OrderUserList, UserList

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderid', 'datecreation', 'orderstatus', 'paymentstatus', 'carelement', 'details', 'liquids', 'amountdamage')
    search_fields = ('orderid', 'orderstatus', 'paymentstatus', 'carelement', 'details', 'liquids')
    list_filter = ('orderstatus', 'paymentstatus')

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('userroleid', 'namerole')
    search_fields = ('namerole',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'login', 'userrole', 'status', 'lastname', 'firstname', 'middlename')
    search_fields = ('login', 'lastname', 'firstname', 'middlename')
    list_filter = ('userrole', 'status')

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('shiftid', 'datestart', 'dateend')
    search_fields = ('shiftid', 'datestart', 'dateend')

@admin.register(OrderUserList)
class OrderUserListAdmin(admin.ModelAdmin):
    list_display = ('orderuserlistid', 'userid', 'orderid')
    search_fields = ('orderuserlistid', 'userid__login', 'orderid__orderid')

@admin.register(UserList)
class UserListAdmin(admin.ModelAdmin):
    list_display = ('userlistid', 'userid', 'shiftid')
    search_fields = ('userlistid', 'userid__login', 'shiftid__shiftid')