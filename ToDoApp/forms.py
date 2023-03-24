from django import forms

from ToDoApp.models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ("__all__")

