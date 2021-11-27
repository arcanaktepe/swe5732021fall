from django import forms
from django.forms.widgets import DateInput, TimeInput

from .models import Post,Service


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','duration','eventdate','eventtime','content','picture','capacity']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            'eventdate':DateInput(attrs={'type': 'date'}),
            'eventtime':TimeInput(attrs={'type': 'time'}),

        }
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title','duration','eventdate','eventtime','content','picture','capacity']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            'eventdate':DateInput(attrs={'type': 'date'}),
            'eventtime':TimeInput(attrs={'type': 'time'}),
        }
