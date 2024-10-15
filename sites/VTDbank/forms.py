import django.forms as forms
from django.forms import ModelForm, Form
from .models import Claims, AppClaims

class ClaimForm(ModelForm):
    class Meta:
        model = Claims
        fields = ["to_user", "amount"]

class GraphForm(Form):
    tz = forms.CharField(max_length=100)

# class AppClaimForm(ModelForm):
#     auto = forms.BooleanField()
#     class Meta:
#         model = AppClaims
#         fields = ["app_name", "target_user", "amount", "auto"]
