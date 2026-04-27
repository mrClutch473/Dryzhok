from django import forms
from .models import VolunteerApplication


class VolunteerApplicationForm(forms.ModelForm):
    """Форма для заявки волонтера"""

    class Meta:
        model = VolunteerApplication
        fields = ['full_name', 'email', 'phone', 'age', 'experience', 'motivation']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваше ФИО',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'example@mail.ru',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+7 (___) ___-__-__',
                'required': True
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ваш возраст',
                'min': 14,
                'max': 100
            }),
            'experience': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Расскажите о вашем опыте общения с животными...',
                'rows': 3
            }),
            'motivation': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Почему вы хотите стать волонтером?',
                'rows': 3
            }),
        }