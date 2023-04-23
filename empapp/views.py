from django.shortcuts import redirect, render
from empapp.forms import AddEmployeeForm, updateEmployeeForm, UserRegistrationForm
from empapp.models import Employee
from django.contrib.auth.decorators import login_required



@login_required
def add_employee_view(request):
    obj = AddEmployeeForm()
    if request.method == 'POST' :
        
        obj = AddEmployeeForm(request.POST , request.FILES)
        if obj.is_valid():
            obj.save()
            return redirect('/emp/list/')


    return render(request, 'empapp/add.html', {'obj':obj})

@login_required
def employee_list(request):
    data = Employee.objects.all()
    return render(request, 'empapp/list.html', {'data': data})

@login_required
def employee_detail(request, id):
    obj = Employee.objects.get(pk = id)
    return render(request, 'empapp/detail.html', {'obj':obj})

@login_required
def update_employee(request, id):
    obj = Employee.objects.get(pk = id)
    form = updateEmployeeForm(instance=obj)
    if request.method == 'POST' :
        form = updateEmployeeForm(request.POST,request.FILES, instance= obj)
        if form.is_valid():
            form.save()
            return redirect(f'/emp/detail/{obj.id}/')
    

    return render(request, 'empapp/update.html', {'obj':obj , 'form':form})

@login_required
def delete_employee(request, id):
    obj = Employee.objects.get(pk = id)
    obj.delete()
    return redirect('/emp/list/')


def user_register_view(request):
    form = UserRegistrationForm()
    print(request.POST)
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    return render(request, 'empapp/register.html', {'form':form})

