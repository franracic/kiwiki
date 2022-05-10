from django import forms

class Editform(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

class Newform(forms.Form):
    title = forms.CharField(max_length=20)
    text = forms.CharField(widget=forms.Textarea)
