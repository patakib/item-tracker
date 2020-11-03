from django import forms
from django.forms import ModelForm

from .models import *

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'starting_date': DateTimeInput(),
            'deadline': DateTimeInput(),
            'action_started': DateTimeInput(),
            'completion_date': DateTimeInput(),
        }
