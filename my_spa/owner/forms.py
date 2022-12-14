from django import forms
from django.forms import ModelForm
from customer.models import *
from owner.models import *

class SlotAddForm(forms.ModelForm):
    class Meta:
        model=Timeslots
        fields=['time','status']
    # timeslot=forms.ChoiceField(choices=Services.SERVICE_TIMESLOT_LIST,required=True)

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


class PackageAddForm(forms.ModelForm):
    class Meta:
        model= Package
        fields ='__all__'


class GiftCardAddForm(forms.ModelForm):
    class Meta:
        model= GiftCards
        fields ='__all__'


class UpdateMembershipForm(forms.ModelForm):
    class Meta:
        model=Memberships
        fields=["name", "validity", "price","desc", "image", "status"]


class UpdateServiceForm(forms.ModelForm):
    class Meta:
        model=Services
        fields=["name", "category", "image","duration", "cost", "description","beautician", "rating","timeslots", "status"]


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields= '__all__'


class UpdateBeauticianForm(forms.ModelForm):
    class Meta:
        model=Beautician
        fields= '__all__'


class UpdateTimeslotForm(forms.ModelForm):
    class Meta:
        model=Timeslots
        fields= '__all__'


class UpdatePackageForm(forms.ModelForm):
    class Meta:
        model=Package
        fields= '__all__'


class UpdateGiftCardForm(forms.ModelForm):
    class Meta:
        model=GiftCards
        fields= '__all__'