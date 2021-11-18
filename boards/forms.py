from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm) :
    class Meta :
        model = Topic
        fields = ['subject', 'message']

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'placeholder': 'what is in your mind?'
            }
        ),
        max_length=2000
    )