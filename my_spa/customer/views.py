from django.shortcuts import render,redirect
from customer.models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,TemplateView,FormView,DetailView,ListView,UpdateView,RedirectView,View
from customer.forms import *
from customer import forms
from django.contrib import messages
import json
from datetime import datetime


# Create your views here.
# path("register", views.RegistrationView.as_view(), name="registration")
class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("login")

#path("",views.LogInView.as_view(),name="login"),
class LogInView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})

#path("home", views.HomeView.as_view(), name="home"),
class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_services=Services.objects.all()
        context["services"]=all_services
        return context

#path("book/<int:sid>", views.BookView.as_view(), name="book")
class BookView(FormView):

    form_class = forms.BookForm
    template_name = "book.html"

    def get(self,request,*args,**kwargs):
        id = kwargs.get("sid")
        service = Services.objects.get(id=id)
        beauticians=Beautician.objects.filter(category=service.category)
        beautician=[b for b in beauticians if b!=1 ]
        a = Timeslots.objects.all()
        a1 = a[::1]
        available_slots = [i for i in a1 if i != 1]
        return render(request,self.template_name,{"form":forms.BookForm(),"service":service,"beautician":beautician,"available_slots":available_slots})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("sid")
        service = Services.objects.get(id=id)
        user = request.user
        timeslot = request.POST.get("slot")
        # date = request.POST.get("date")
        selected_beautician=request.POST.get("beauty") # Fetch selected beautician

        if (timeslot) and (selected_beautician):
            BookedSlot.objects.create(booked_slots=timeslot)
            booked_slot=BookedSlot.objects.filter(booked_slots=timeslot)[0]
            beautician=Beautician.objects.filter(name=selected_beautician)[0]
            booking=Booking.objects.create(services=service,user=user,timeslot=booked_slot,beautician=beautician,cost=service.cost)
            Timeslots.objects.filter(time=timeslot).delete()
            m="Hello User, Your booking request initiated and the order id is: ",booking.id ,". Thank you!"
            messages.success(request, m)
        else:
            m="Sorry! Your booking request failed! Please make sure you selected preferred timeslot & beautician , thank you!"
            messages.warning(request,m)
        return redirect("home")






#path("mybookings", views.MyBookingView.as_view(), name="bookings")
class MyBookingView(ListView):
    template_name = "bookings.html"
    model = Booking
    context_object_name = 'bookings'


    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).exclude(status="cancelled")

        # def delete_service(self, request, *args, **kwargs):
        #     a = Services.objects.all()
        #     a.delete()
        #
        # print(Booking.objects.filter(user=self.request.user))


#path("mybookings/<int:bid>", views.BookingUpdateView.as_view(), name="update-booking"),
class BookingUpdateView(UpdateView):
    model = Booking
    template_name = "booking-update.html"
    pk_url_kwarg = "bid"
    success_url = reverse_lazy("bookings")
    form_class = UpdateBookingForm


    def form_valid(self, form):
        messages.success(self.request,"Booking  updated successfully")
        return super().form_valid(form)

#path("mybookings/<int:bid>/cancel", views.cancel_booking, name="cancel-booking"),
class CancelBookingView(View):
    # model = Booking
    # template_name = "confirm-cancel.html"
    # pk_url_kwarg = "bid"
    # success_url = reverse_lazy("home")
    # form_class = CancelBookingForm
    def get(self,request,*args,**kwargs):
        id = kwargs.get("bid")
        booking = Booking.objects.get(id=id)
        return render(request,"confirm-cancel.html",{"booking":booking})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("bid")
        booking = Booking.objects.get(id=id)
        print(booking)
        booking.status="cancelled"
        booking.save()
        msg="Hello User booking cancelled as per your request"
        messages.success(request,msg)
        return redirect('home')



#path("slots", views.AddSlots.as_view(), name="add-slot")
#Admin action
#Pending
class AddSlots(TemplateView):
    template_name = "add-slots.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_services = Services.objects.all()
        context["services"] = all_services
        a=Timeslots.objects.all()
        a1=a[::1]
        p=[i for i in a1 if i!=1 ]
        context["slots"]=p
        return context

    def post(self,request,*args,**kwargs):
        data=request.POST.get("slot")
        print("Fetched data is ",data)
        return redirect("home")

#path("slots/update", views.UpdateSlots.as_view(), name="update-slot"),
class UpdateSlots(FormView):
    form_class = AddSlotForm
    template_name = "update-slots.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # all_services = Services.objects.all()
        # context["services"] = all_services
        a=Timeslots.objects.all()
        a1=a[::1]
        p=[i for i in a1 if i!=1 ]
        context["slots"]=p
        return context


    def post(self, request, *args, **kwargs):
        id=kwargs.get("sid")
        service=Services.objects.filter(id=id)

        del_slot=request.POST.get("slot")
        # slot = request.POST['timeslot']
        slot = request.POST.get('timeslot')
        booked_slot=BookedSlot.objects.filter(booked_slots=slot)
        print(booked_slot)

        print("Fetched slot is : ",slot)
        print("Slot to remove : ", del_slot)
        if slot:
            if booked_slot:
                msg="Sorry! Selected slot already booked by an user"
                messages.warning(request,msg)
                return redirect("update-slot")
            else:
                Timeslots.objects.create(time=slot)
                messages.success(request,"Selected slot added successfully")
                return redirect("update-slot")
        else:
            Timeslots.objects.filter(time=del_slot).delete()
            messages.warning(request, "Selected slot removed successfully")
            return redirect("update-slot")

#path("category/add", views.AddCategories.as_view(), name="add-category"),
class AddCategories(CreateView):
    template_name = "add-categories.html"
    form_class =forms.CategoryAddForm
    success_url =reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"]=Categories.objects.all()
        return context

    # def post(self, request, *args, **kwargs):
    #     form = forms.CategoryAddForm(request.POST)
    #     if form.is_valid():
    #         category_name = form.cleaned_data.get("category_name")
    #         description = form.cleaned_data.get("description")
    #         status = form.cleaned_data.get("status")
    #         image = form.cleaned_data.get("image")
    #         print(category_name,description,status,image)
    #         Categories.objects.create(category_name=category_name,description=description,status=status,image=image)
    #         msg=category_name,"added succesfully"
    #         messages.success(request,msg)
    #         return redirect("home")

# path("services/add", views.AddServices.as_view(), name="add-service"),
class AddServices(CreateView):
    form_class = ServiceAddForm
    template_name = "add-services.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"]=Services.objects.all()
        return context














