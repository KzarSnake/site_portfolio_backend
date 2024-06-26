from django.forms import ModelForm

from .models import Mail


class MailForm(ModelForm):
    class Meta:
        model = Mail
        fields = ['name', 'phone_number', 'contact', 'memo']
