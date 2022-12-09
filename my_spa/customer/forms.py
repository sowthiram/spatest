from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from customer.models import *
from datetime import date
from customer.models import *
import datetime
# from datetimewidget.widgets import DateTimeWidget

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {

            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),

        }

class DatePicker(forms.DateInput):
    input_type = 'date'

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ('date', 'timeslot')
#         widgets = {
#             'date': DatePicker(),
#         }


class BookForm(forms.Form):

    timeslot=forms.ChoiceField(choices=Services.SERVICE_TIMESLOT_LIST,required=True)

class AddSlotForm(forms.Form):

    timeslot=forms.ChoiceField(choices=Services.SERVICE_TIMESLOT_LIST,required=True)


class UpdateBookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["timeslot", "beautician"]

class CancelBookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["status"]

class CategoryAddForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields=["category_name","description","status","image"]

class ServiceAddForm(forms.ModelForm):
    class Meta:
        model= Services
        fields = ['name','category','image','duration','cost','description','beautician','status','timeslots']