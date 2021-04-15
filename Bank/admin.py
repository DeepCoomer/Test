from django.contrib import admin
from Bank.models import Contact
from Bank.models import Customer
from Bank.models import Bank_statement
from Bank.models import Transfer_money

# Register your models here.

admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Bank_statement)
admin.site.register(Transfer_money)