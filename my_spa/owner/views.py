from django.shortcuts import render,redirect
from customer.models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,TemplateView,FormView,DetailView,ListView,UpdateView,RedirectView,View
from django.contrib import messages
from owner.forms import*

# Create your views here.
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
    form_class =CategoryAddForm
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
