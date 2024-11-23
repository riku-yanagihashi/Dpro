from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'お名前',
            'email': 'メールアドレス',
            'message': 'お問い合わせ内容',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'お名前'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'メールアドレス'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'お問い合わせ内容'}),
        }
