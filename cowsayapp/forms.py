from django import forms


class CowsayText(forms.Form): 
    textline = forms.CharField(max_length=80)