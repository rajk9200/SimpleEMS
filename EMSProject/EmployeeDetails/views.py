from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
from .models import Employee,Cities
from .forms import EmployeeForm,NewEmployeeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.core import serializers


def employeeAdd(request):
    form =NewEmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('emp')
        print('new Employee Added')
    context ={
       'form':form
    }
    return render(request,'addEmp.html',context)


def employeeDetails(request):
    all_employees = Employee.objects.all()
    if 'sname' in request.POST:
        name1 =request.POST.get('sname')
        all_employees = Employee.objects.filter(Q(name__startswith=name1))

    page = request.GET.get('page', 1)

    paginator = Paginator(all_employees, 10)
    try:
        all_employee = paginator.page(page)
    except PageNotAnInteger:
        all_employee = paginator.page(1)
    except EmptyPage:
        all_employee = paginator.page(paginator.num_pages)

    context ={
       'all_employee':all_employee,

    }
    return render(request,'index.html',context)

def homepage(request):

    return render(request,'index.html')

def employeeEdit(request,id=None):
    empObj =Employee.objects.get(id=id)
    form =EmployeeForm(request.POST or None, instance=empObj)
    if form.is_valid():
        form.save()
        return redirect('emp')
    context ={
       'form':form
    }
    return render(request,'edit.html',context)



def employeeDelete(request,id=None):

    if request.method=='POST':

        empObj = Employee.objects.get(id=id)
        empObj.delete()
        print('delete ho gya')
        return redirect('emp')

    return render(request,'delete.html')


def getCities(request):
    response={}
    if request.is_ajax():
        selectCity = request.GET.get('selectCity')
        print(selectCity)
        cities =Cities.objects.filter(Q(name__startswith=selectCity))
        response = serializers.serialize("json", cities)
    return HttpResponse(response, content_type='application/json')