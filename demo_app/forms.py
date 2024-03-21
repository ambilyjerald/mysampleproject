from django import forms
from demo_app.models import todo
class todo_form(forms.ModelForm):
    class Meta:
        model=todo
        fields=("__all__")
