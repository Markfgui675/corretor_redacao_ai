from django import forms
from corretor_ia.models import Redacao

class RedacaoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Redacao
        fields = '__all__'
        widgets = {
            'redacao':forms.Textarea(
                attrs={
                    'placeholder':'Sua redação aqui',
                    'class':'box-send-textarea full-width',
                    'cols':'80',
                    'rows':'5'
                }
            )
        }

