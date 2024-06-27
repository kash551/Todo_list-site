from django import forms
from .models import Todo, UserProfile


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"        