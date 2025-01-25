from django import forms
from utils.django_forms import add_placeholder
from django.contrib.auth.models import User


class LogInForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['usuario'], 'digite seu usuario')
        add_placeholder(self.fields['senha'], 'digite sua senha')

    usuario = forms.CharField()
    senha = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['usuario', 'senha']
