from django.forms import ModelForm
from django import forms
from .models import Post, Comentario

class FormPost(ModelForm):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'categoria',
            'body',
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),           
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }