from tkinter.ttk import LabeledScale
from django import forms
from empapp.models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class updateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        

        labels ={
            'name' : "Updated Name",
            'salary' : "Updated Salary",
            'emp_id' : "Updated Emp ID",
            }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

