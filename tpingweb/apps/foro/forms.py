from django.forms import ModelForm
from django import forms
from .models import Post, Comentario, Denuncia

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
    
class FormComentario(ModelForm):
    class Meta:
        model = Comentario
        fields = [
            'body',
        ]

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
    
class FormDenuncia(ModelForm):
    class Meta:
        model = Denuncia
        fields = [
            'texto',
        ]
        widgets = {
            'texto': forms.Textarea(attrs={'class':'form-control'}),
        }