from django import forms
from django.contrib.auth.models import User
from utils.django_forms import add_placeholder, strong_password


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password',
                  'password_repeat']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Usuario')
        add_placeholder(self.fields['email'], 'E-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: Filipe')
        add_placeholder(self.fields['last_name'], 'Ex.: Jose')
        add_placeholder(self.fields['password'], 'Sua senha')
        add_placeholder(self.fields['password_repeat'], 'Repita sua senha')

    first_name = forms.CharField(
        error_messages={
            'required': 'Escreva seu primeiro nome aqui',
        },
        label='Seu primeiro nome'
    )
    last_name = forms.CharField(
        error_messages={
            'required': 'Escreva seu Sobrenome',
        },
        label='Sobrenome'
    )
    username = forms.CharField(
        help_text={
            'max_length': 'O nome de usuário deve ter entre 4 e 150 caracteres',
        },
        error_messages={
            'required': 'Este campo não deve estar vazio',
            'min_length': 'O nome de usuário deve ter pelo menos 4 caracteres',
            'max_length': 'O nome de usuário deve ter menos de 150 caracteres',
            'unique': 'Este nome de usuário já existe',
        },
        label='Seu Usuario',
        max_length=150,
        min_length=4,

    )
    email = forms.EmailField(
        error_messages={
            'required': 'Endereço de e-mail inválido',
            'unique': 'Este endereço de e-mail já existe.',
        },
        label='E-mail',
    )
    password = forms.CharField(
        error_messages={
            'required': 'A senha não deve estar vazia',
        },
        label='Sua Senha',
        validators=[strong_password],
        widget=forms.PasswordInput,
    )
    password_repeat = forms.CharField(
        error_messages={
            'required': 'Por favor, repita sua espada aqui',
        },
        label='Repita sua senha',
        widget=forms.PasswordInput,
    )

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError(
                'Este endereço de e-mail já existe.', code='invalid')
        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password != password_repeat:
            password_confirmation_error = forms.ValidationError(
                'A senha e o password_repeat devem ser iguais',
                code='invalid'
            )
            raise forms.ValidationError({
                'password': password_confirmation_error,
                'password_repeat': [
                    password_confirmation_error,
                ],
            })
