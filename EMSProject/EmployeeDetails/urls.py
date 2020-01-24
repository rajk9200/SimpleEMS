
from django.urls import path
from . import views as EMSp
urlpatterns = [
    path('', EMSp.employeeDetails, name='emp'),
    path('addEmployee/', EMSp.employeeAdd, name='addEmp'),
    path('edit/<int:id>/', EMSp.employeeEdit, name='edit_emp'),
    path('delete/<int:id>/', EMSp.employeeDelete, name='del_emp'),
    path('getCities/', EMSp.getCities, name='getCities'),
]