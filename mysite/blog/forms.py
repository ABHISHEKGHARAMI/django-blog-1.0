# build the form to share the content to the user email
from django import forms
from .models import Comment

# class for the form template
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to  = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )
    
    
# creating the form for the comment for the user
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']

