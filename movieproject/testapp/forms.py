from django import forms
from testapp.models import moviemodel
from testapp.models import dummimodel

class movieform(forms.ModelForm):
    class Meta:
        model=moviemodel
        fields='__all__'
class movie1form(forms.ModelForm):
    class Meta:
        model=dummimodel
        fields='__all__'
