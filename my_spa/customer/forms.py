from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from customer.models import *
from datetime import date
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

# class BookForm(forms.Form):

#     timeslot=forms.ChoiceField(choices=Services.SERVICE_TIMESLOT_LIST,required=True)

class BookForm(forms.Form):
    time=forms.CheckboxInput()




class UpdateBookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["timeslot", "beautician"]

class CancelBookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["status"]

