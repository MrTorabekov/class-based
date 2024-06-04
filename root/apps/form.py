from django import forms
from .models import People


# creating a form
class UpdateForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'
