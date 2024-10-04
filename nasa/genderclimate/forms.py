from django import forms
from  .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'gender', 'location', 'health_condition', 'email', 'phone', 'next_of_kin']
        
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}),
            'health_condition': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'next_of_kin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Next of kin phone number'}),
        }
        
        labels = {
            'age': 'Age',
            'gender': 'Gender',
            'location': 'Location',
            'health_condition': 'Health Condition',
            'email': 'Email',
            'phone': 'Phone Number',
            'next_of_kin': 'Next of Kin',
        }