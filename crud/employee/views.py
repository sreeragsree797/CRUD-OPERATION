from django.shortcuts import render,redirect
from employee.models import Employee
from employee.forms import EmployeForm
# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeForm()
    return render(request,'index.html',{'form' :form})

def show(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employee':employees})
def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    
    return render(request,'edit.html',{'employee' :employee})

def destroy(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
        
                