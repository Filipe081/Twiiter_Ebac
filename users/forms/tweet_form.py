from django import forms
from tweeter.models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    content = forms.CharField(
        max_length=140,
        error_messages={
            'required': 'Tweet content is required',
            'max_length': 'Tweet content cannot exceed 140 characters',
            'min_length': 'Tweet content must have at least 1 characters',
        },
        widget=forms.Textarea(
            attrs={
                'placeholder': 'O que está acontecendo?',
                'class': 'textarea-input',
                'rows': 4,
                'accept-charset': 'UTF-8',
            },
        ),
    )

    def clean(self):
        content = self.cleaned_data.get('content')
        if len(content) < 1:
            raise forms.ValidationError(
                'Tweet must have at least 1 characters.')
        return super().clean()
