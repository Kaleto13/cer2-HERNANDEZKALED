from django import forms
from miapp.models import *

class Comunicado_form(forms.ModelForm):
    class Meta:
        model = Comunicado
        fields = "__all__"