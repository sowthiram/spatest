from django.urls import path
from customer import views

app_name = "customer"
urlpatterns=[
    path("",views.LogInView.as_view(),name="login"),
    path("register", views.RegistrationView.as_view(), name="registration"),
    path("home", views.HomeView.as_view(), name="home"),
    path("book/<int:sid>", views.BookView.as_view(), name="book"),
    path("mybookings", views.MyBookingView.as_view(), name="bookings"),
    path("mybookings/<int:bid>", views.BookingUpdateView.as_view(), name="update-booking"),
    path("slots", views.AddSlots.as_view(), name="add-slot"),
    path("slots/update", views.UpdateSlots.as_view(), name="update-slot"),
    path("category/add", views.AddCategories.as_view(), name="add-category"),
    path("services/add", views.AddServices.as_view(), name="add-service"),
    path("mybookings/<int:bid>/cancel", views.CancelBookingView.as_view(), name="cancel-booking"),
]