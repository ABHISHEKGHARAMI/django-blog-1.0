# build the form to share the content to the user email
from django import forms

# class for the form template
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to  = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )
    

