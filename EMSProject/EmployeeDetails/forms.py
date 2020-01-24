from django import forms
from .models import Employee
import re
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =('email','city')

    # age = forms.CharField(max_length=3,widget=forms.TextInput(attrs={'type':'number'}))

    # pan_number = forms.CharField(widget=forms.TextInput(attrs={'disabled':'true'}))
    # name = forms.CharField(widget=forms.TextInput(attrs={'disabled':'true'}))
    # gender = forms.CharField(widget=forms.TextInput(attrs={'disabled':'true'}))



class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields =('name','pan_number','age','gender','email','city')

    age = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'type': 'number'}))

    def clean_pan_number(self):
        pan_number = self.cleaned_data.get('pan_number')
        pan_pattern =r'^[A-Z]{5}[0-9]{4}[A-Z]$'
        if not (re.match(pan_pattern,pan_number)):
            raise forms.ValidationError("Please Enter Valid Pan Number")
        return pan_number

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if not (int(age) <= 100 and int(age) >=1):
            raise forms.ValidationError("Age must be 1-100")
        return age