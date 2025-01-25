from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'rows': 2,
                    'cols': 50,
                    'placeholder': 'Enviar Comentario...',
                    'class': 'comment-input',
                })
        }
