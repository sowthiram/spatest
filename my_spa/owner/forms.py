from django import forms
from django.forms import ModelForm
from customer.models import *
from owner.models import *

class AddSlotForm(forms.Form):

    timeslot=forms.ChoiceField(choices=Services.SERVICE_TIMESLOT_LIST,required=True)

class CategoryAddForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields=["category_name","description","status","image"]

class ServiceAddForm(forms.ModelForm):
    class Meta:
        model= Services
        fields = ['name','category','image','duration','cost','description','beautician','status','timeslots']

class MembershipAddForm(forms.ModelForm):
    class Meta:
        model= Memberships
        fields ='__all__'

class BeauticianAddForm(forms.ModelForm):
    class Meta:
        model= Beautician
        fields ='__all__'