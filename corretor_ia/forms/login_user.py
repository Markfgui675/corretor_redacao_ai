from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class':'full-width',
                'placeholder':'Digite seu e-mail'
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'class':'full-width',
                'placeholder':'Digite sua senha'
            }
        )
    )
