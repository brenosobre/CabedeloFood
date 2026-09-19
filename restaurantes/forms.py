from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['autor', 'estrelas', 'comentario']
        labels = {
            'autor': 'Seu Nome',
            'estrelas': 'Nota (Estrelas)',
            'comentario': 'Feedback'
        }
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'estrelas': forms.Select(attrs={'class': 'form-select'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'O que achou do lugar?'}),
        }