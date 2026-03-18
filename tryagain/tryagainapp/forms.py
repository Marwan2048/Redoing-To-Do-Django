from django import forms
from .models import Task
class FormTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["Name","Brief","Important"]
        widgets = {"Name": forms.TextInput(attrs={"placeholder": "Task Name"}),
                   "Important":forms.RadioSelect,}
        