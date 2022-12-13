from django.contrib import admin
from customer.models import *
from owner.models import*
# Register your models here.
admin.site.register(Categories)
admin.site.register(Beautician)
admin.site.register(Services)
admin.site.register(Booking)
admin.site.register(BookedSlot)
admin.site.register(Timeslots)
admin.site.register(Memberships)

