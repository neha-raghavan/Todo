from django import forms
from .models import *
from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = "time"

 
class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'desc', 'due_date', 'time']
    widgets = {
            'due_date': DateInput(),
            'time':TimeInput(),
        }

    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['username','first_name','email', 'password1', 'password2']