from django.db import models
from django.contrib.auth.models import AbstractUser

class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    datecreation = models.DateField("Date Creation", auto_now_add=True)
    orderstatus = models.CharField("Order Status", max_length=255, default='готовится')
    paymentstatus = models.CharField("Payment Status", max_length=255, default='принят')
    carelement = models.CharField("Car Element", max_length=255)
    details = models.CharField("Details", max_length=255)
    liquids = models.CharField("Liquids", max_length=255)
    amountdamage = models.IntegerField("Amount Damage")

    def __str__(self):
        return f"Order {self.orderid} - {self.orderstatus}"

class UserRole(models.Model):
    userroleid = models.AutoField(primary_key=True)
    namerole = models.CharField("Role Name", max_length=255)

    def __str__(self):
        return self.namerole

class User(AbstractUser):
    ROLE_CHOICES = (
        ('master', 'Мастер приемщик'),
        ('automachenic', 'Автомеханик'),
        ('autodiagnostic', 'Автодиагност'),
    )
    STATUS_CHOICES = (
        ('active', 'Работает'),
        ('dismissed', 'Уволен'),
    )
    userid = models.AutoField(primary_key=True)
    login = models.CharField("Login", max_length=255)
    userrole = models.CharField(max_length=20, choices=ROLE_CHOICES)
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES)
    middlename = models.CharField("Middle Name", max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['userrole']

    def __str__(self):
        return self.username

# class User(models.Model):
#     userid = models.AutoField(primary_key=True)
#     login = models.CharField("Login", max_length=255)
#     password = models.CharField("Password", max_length=255)
#     userrole = models.ForeignKey(UserRole, on_delete=models.CASCADE)
#     status = models.CharField("Status", max_length=255, null=True, blank=True)
#     lastname = models.CharField("Last Name", max_length=255)
#     firstname = models.CharField("First Name", max_length=255)
#     middlename = models.CharField("Middle Name", max_length=255, null=True, blank=True)

#     def __str__(self):
#         return self.login

class Shift(models.Model):
    shiftid = models.AutoField(primary_key=True)
    datestart = models.DateField("Date Start")
    dateend = models.DateField("Date End")

    def __str__(self):
        return f"Shift {self.shiftid} - {self.datestart} to {self.dateend}"

class OrderUserList(models.Model):
    orderuserlistid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"OrderUserList {self.orderuserlistid}"

class UserList(models.Model):
    userlistid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    shiftid = models.ForeignKey(Shift, on_delete=models.CASCADE) # РОФ

    def __str__(self):
        return f"UserList {self.userlistid}"
