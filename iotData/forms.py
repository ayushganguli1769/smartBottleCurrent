from django import forms
class taskForm(forms.Form):
    prescription = forms.CharField(max_length=100)
    end = DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"])
