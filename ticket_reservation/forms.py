from django import forms
from django.contrib.auth.models import User


class TicketForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label=None,
        label='Select User')
