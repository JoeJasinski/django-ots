from django import forms
from . import models


class SecretForm(forms.ModelForm):

    class Meta:
        model = models.Secret
        fields = ['text', 'expire_date', 'expire_max_count', 'require_login']
