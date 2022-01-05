from django import forms
from django.db.models import fields
from .models import StorageSixA, StorageSixB, StorageSixC, StorageSixE

# Django ModelForm is a class that is used to directly convert a model into a Django form.

class SixAForm(forms.ModelForm):
    class Meta:
        model = StorageSixA
        fields = "__all__"
        
class SixBForm(forms.ModelForm):
    class Meta:
        model = StorageSixB
        fields = "__all__"

class SixCForm(forms.ModelForm):
    class Meta:
        model = StorageSixC
        fields = "__all__"

class SixEForm(forms.ModelForm):
    class Meta:
        model = StorageSixE
        fields = "__all__"


