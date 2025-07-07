from django import forms
from homepage.models import CustomUser, PatientProfile
from django.core.exceptions import ValidationError
import re

class PatientSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

  

    age = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    diabetes_type = forms.ChoiceField(
        choices=[
            ('Type 1', 'Type 1'),
            ('Type 2', 'Type 2'),
            ('Gestational', 'Gestational')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # تحقق من تطابق كلمتي السر
        if password != confirm_password:
            raise ValidationError("كلمتا السر غير متطابقتين.")
        if password:

         if len(password) < 8:
             raise ValidationError("Password must be at least 8 characters long.")
         if not re.search(r'[A-Z]', password):
             raise ValidationError("Password must contain at least one uppercase letter.")
         if not re.search(r'[a-z]', password):
             raise ValidationError("Password must contain at least one lowercase letter.")
         if not re.search(r'[0-9]', password):
             raise ValidationError("Password must contain at least one number.")
         if not re.search(r'[@#$%^&*!]', password):
             raise ValidationError("Password must contain at least one special character (e.g. @, #, !).")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email is pre-registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_medical_staff = False
        if commit:
            user.save()
            PatientProfile.objects.create(
                user=user,
               
                gender=self.cleaned_data['gender'],
                
                age=self.cleaned_data['age'],
                diabetes_type=self.cleaned_data['diabetes_type'],
                phone=self.cleaned_data['phone'],
            )
        return user
