from dataclasses import fields
from django import forms
from employee.models import Employee

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"