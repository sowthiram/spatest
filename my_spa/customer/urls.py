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
    path("mybookings/<int:bid>/cancel", views.CancelBookingView.as_view(), name="cancel-booking"),
    path("shop", views.ShopView.as_view(), name="shop"),
    path("membership", views.MembershipView.as_view(), name="memberships"),

]