from django.forms import ModelForm
from .models import Post
from django import forms
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'postcategory']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title', False)
        if title:
            return title
        else:
            raise forms.ValidationError("Title Required")

    def clean_image(self, *args, **kwargs):
        image = self.cleaned_data.get('image', False)
        if image:
            return image
        else:
            raise forms.ValidationError("No image found")

