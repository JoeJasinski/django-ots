from django import forms
from django.utils import timezone
from . import MAX_EXPIRATION_TIME
from . import models
from . import td_utils


class SecretForm(forms.ModelForm):

    def clean_expire_date(self):
        now = timezone.now()
        future = now + td_utils.convert_to_timedelta(MAX_EXPIRATION_TIME)
        data = self.cleaned_data.get('expire_date')
        print("JJJ", data, future, now)
        if data and data > future:
            raise forms.ValidationError(
                "This date cannot be larger than "
                "{0.month}/{0.day}/{0.year} {0.hour}:{0.minute}".format(future))
        return data

    class Meta:
        model = models.Secret
        fields = [
            'text', 'expire_date',
            'expire_max_count', 'require_login', 'page_refresh']
