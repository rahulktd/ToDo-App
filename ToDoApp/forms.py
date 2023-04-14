from django import forms

from ToDoApp.models import ToDo


class Dateinput(forms.DateInput):
    input_type = 'date'

class ToDoForm(forms.ModelForm):
    date = forms.DateField(widget=Dateinput)
    class Meta:
        model = ToDo
        fields = ('event','date')

