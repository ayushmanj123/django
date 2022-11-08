from django import forms
from django.forms import ModelForm
from .models import Aadhar_Front, Aadhar_Back

class AadharFront(ModelForm):
    class Meta:
        model = Aadhar_Front
        fields = ('aadhar_front',)

        labels = {
            'aadhar_front':'',
        }

class AadharBack(ModelForm):
        class Meta:
            model = Aadhar_Back
            fields = ('aadhar_back',)

            labels = {
                'aadhar_back':'',
            }
