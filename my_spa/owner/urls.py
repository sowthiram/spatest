from django.urls import path
from owner import views


urlpatterns=[
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("slots", views.AddSlots.as_view(), name="add-slot"),
    path("slots/update", views.UpdateSlots.as_view(), name="update-slot"),
    path("category/add", views.AddCategories.as_view(), name="add-category"),
    path("services/manage", views.ManageServices.as_view(), name="add-service"),
    path("services/<int:sid>", views.ServiceView.as_view(), name="view-service"),
    path("account", views.AdminAccountView.as_view(), name="account-settings"),
    path("memberships/manage", views.ManageMemberships.as_view(), name="manage-memberships"),
    path("memberships/add", views.AddMemberships.as_view(), name="add-memberships")
]