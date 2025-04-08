from django import forms
from ..models.Activity import Activity

class AnswerForm(forms.Form):
    answer = forms.CharField(label='Tu respuesta', max_length=200)

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'description', 'image', 'date']