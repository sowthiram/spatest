from django.urls import path
from owner import views


urlpatterns=[
    path("slots", views.AddSlots.as_view(), name="add-slot"),
    path("slots/update", views.UpdateSlots.as_view(), name="update-slot"),
    path("category/add", views.AddCategories.as_view(), name="add-category"),
    path("services/add", views.AddServices.as_view(), name="add-service"),
]