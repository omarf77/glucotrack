
from django import forms
from .models import AddEntry

class BloodSugarReadingForm(forms.ModelForm):
    class Meta:
        model = AddEntry
        fields = ['blood_sugar', 'date', 'reading_type', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
