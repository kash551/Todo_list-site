from django import forms
from .models import To_do


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"