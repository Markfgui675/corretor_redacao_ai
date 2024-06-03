from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class':'full-width',
                'placeholder':'Digite o username'
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'class':'full-width',
                'placeholder':'Digite a senha'
            }
        )
    )
