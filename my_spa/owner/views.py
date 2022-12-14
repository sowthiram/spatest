from django.shortcuts import render,redirect
from customer.models import *
from owner.models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView,TemplateView,FormView,DetailView,ListView,UpdateView,RedirectView,View
from django.contrib import messages
from owner.forms import*

# Create your views here.

class DashboardView(TemplateView):
    template_name="index.html"
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context["bookings"]=Booking.objects.all()
        return context

class AdminAccountView(TemplateView):
    template_name="account-settings.html"
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context["services"]=Services.objects.all()
        return context



#path("slots", views.AddSlots.as_view(), name="add-slot")
#Admin action
#Pending
class AddSlots(TemplateView):
    template_name = "add-slots.html"

    def get_context_data(self,request,*args,**kwargs):
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


#Categories
class ManageCategoriesView(TemplateView):
    model=Categories
    template_name = "manage-categories.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"]=Categories.objects.all()
        return context

class AddCategoriesView(CreateView):
    template_name = "add-categories.html"
    form_class =CategoryAddForm
    success_url =reverse_lazy("manage-categories")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"]=Categories.objects.all()
        return context

#Services
class ManageServicesView(TemplateView):
    model=Services
    template_name = "manage-services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"]=Services.objects.all()
        return context

class AddServicesView(FormView):
    template_name = "add-services.html"
    form_class =ServiceAddForm
    success_url =reverse_lazy("manage-services")

    def post(self, request,*args,**kwargs):
        form=ServiceAddForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request,"Service created Successfully")
            return render(request,"manage-services.html")
        else:
            messages.warning(request,"Service creation failed")
            return redirect("manage-services")
    
class ServiceView(DetailView):
    model=Services
    template_name="service-view.html"
    context_object_name= "service"
    pk_url_kwarg="sid"

#Memberships
class ManageMembershipsView(TemplateView):
    model=Memberships
    template_name="manage-memberships.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["membership"]=Memberships.objects.all()
        return context

class AddMembershipsView(FormView):
    template_name = "add-memberships.html"
    form_class =MembershipAddForm
    success_url =reverse_lazy("manage-memberships")

    def post(self, request,*args,**kwargs):
        form=MembershipAddForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request,"Membership created Successfully")
            return render(request,"manage-memberships.html")
        else:
            messages.warning(request,"Membership creation failed")
            return redirect("manage-memberships")

#Beauticians
class ManageBeauticiansView(TemplateView):
    model=Beautician
    template_name = "manage-beauticians.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beauticians"]=Beautician.objects.all()
        return context

class AddBeauticiansView(CreateView):
    template_name = "add-beauticians.html"
    form_class =BeauticianAddForm
    success_url =reverse_lazy("manage-beauticians")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beauticians"]=Beautician.objects.all()

        category=Beautician.objects.filter(category__category_name="Manicure")
        print("Category is: ",category)
        
        return context

    def post(self, request,*args,**kwargs):
        form=BeauticianAddForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,"Beautician added Successfully")
            return render(request,"manage-beauticians.html")
        else:
            messages.warning(request,"Beautician creation failed")
            return redirect("manage-beauticians")

#Timeslots
class ManageTimeslotsView(TemplateView):
    model=Timeslots
    template_name = "manage-timeslots.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeslots"]=Timeslots.objects.all()
        return context

class AddTimeslotsView(CreateView):
    template_name = "add-timeslots.html"
    form_class =SlotAddForm
    success_url =reverse_lazy("manage-timeslots")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timeslots"]=Timeslots.objects.all()
        return context
    
    def post(self, request,*args,**kwargs):
        form=SlotAddForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,"Timeslot created Successfully")
            return render(request,"manage-timeslots.html")
        else:
            messages.warning(request,"Timeslot creation failed")
            return redirect("manage-timeslots")

# #path("slots/update", views.UpdateSlots.as_view(), name="update-slot"),
# class UpdateSlots(FormView):
#     template_name = "manage-timeslots.html"
#     form_class = AddSlotForm
#     success_url =reverse_lazy("manage-timeslots.html")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         a=Timeslots.objects.all()
#         a1=a[::1]
#         p=[i for i in a1 if i!=1 ]
#         context["slots"]=p
#         return context


#     def post(self, request, *args, **kwargs):
#         id=kwargs.get("sid")
#         service=Services.objects.filter(id=id)

#         del_slot=request.POST.get("slot")
#         # slot = request.POST['timeslot']
#         slot = request.POST.get('timeslot')
#         booked_slot=BookedSlot.objects.filter(booked_slots=slot)
#         print(booked_slot)

#         print("Fetched slot is : ",slot)
#         print("Slot to remove : ", del_slot)
#         if slot:
#             if booked_slot:
#                 msg="Sorry! Selected slot already booked by an user"
#                 messages.warning(request,msg)
#                 return redirect("update-slot")
#             else:
#                 Timeslots.objects.create(time=slot)
#                 messages.success(request,"Selected slot added successfully")
#                 return redirect("update-slot")
#         else:
#             Timeslots.objects.filter(time=del_slot).delete()
#             messages.warning(request, "Selected slot removed successfully")
#             return redirect("update-slot")

        
    

    
