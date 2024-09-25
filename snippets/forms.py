from django import forms


class SnippetForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)
    description = forms.CharField(widget=forms.Textarea(), required=False)
    code = forms.CharField(widget=forms.HiddenInput(), required=True)
    language = forms.CharField(widget=forms.Select(), max_length=100)
