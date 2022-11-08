from django import forms
from django.forms import ModelForm
from .models import Aadhar_Front, Aadhar_Back

class AadharFront(ModelForm):
    class Meta:
        model = Aadhar_Front
        fields = ('name','aadhar_front',)

        labels = {
            'name':'',
            'aadhar_front':'',
        }
        widgets = {
              'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
        }
    
class AadharBack(ModelForm):
        class Meta:
            model = Aadhar_Back
            fields = ('name','aadhar_back',)

            labels = {
                'name': '',
                'aadhar_back':'',
            }
            widgets = {
              'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
        }