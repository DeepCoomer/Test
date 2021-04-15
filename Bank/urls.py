from django.contrib import admin
from django.urls import path,include
from Bank import views

urlpatterns = [
    path('',views.index,name='index'),
    path('data',views.CustomerData,name='data'),
    # path('data',views.data,name='data'),
    path('admistration',views.CustomerData, name="admistration"),
    # path('logout',views.logoutUser, name="logout"),
    path('bank_statement',views.bank_statement,name="bank_statement"),
    path('bank_statement_details',views.bank_statement_details,name="bank_statement_details"),
    path('transfer_money',views.transfer_money,name="transfer_money"),
    path('transfer_history',views.transfer_history,name="transfer_history")
]
