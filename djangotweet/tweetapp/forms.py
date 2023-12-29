from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = f"{visible.field.label}..."
                
    name_input = forms.CharField(label="Name", max_length=20)
    surname_input = forms.CharField(label="Surname", max_length=20)
    message_input = forms.CharField(label="Message", max_length=500, widget=forms.Textarea(attrs={"rows": "5"}))

class AddTweetModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = f"{visible.field.label}"
    
    class Meta:
        model = Tweet
        fields = ['name', 'surname', 'username', 'message']
        
