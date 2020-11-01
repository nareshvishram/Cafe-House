from django.forms import ModelForm
from django import forms
from .models import *

class About_Edit_Form(forms.ModelForm):
    class Meta:
        model=About
        exclude=()
        widgets={
            "about": forms.Textarea(attrs={ "rows": "10"}),
        }

class Item_Model_Form(forms.ModelForm):
    class Meta:
        model=Item
        exclude=()
        widgets={
            "title":forms.TextInput(attrs={"id":"song","required":""}),
            "description":forms.Textarea(attrs={"rows":"10","required":""}),
            "ingredients":forms.Textarea(attrs={"rows":"10","required":""}),
            "price":forms.NumberInput(attrs={"id":"song","required":""}),
            "day":forms.NumberInput(attrs={"id":"song","required":""}),
            "image":forms.FileInput(attrs={"required":""})
        }