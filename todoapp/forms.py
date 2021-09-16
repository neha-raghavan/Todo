from django import forms
from .models import Task
from bootstrap_datepicker_plus import DateTimePickerInput

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

    