from django.urls import path
from owner import views


urlpatterns=[
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("slots", views.AddSlots.as_view(), name="add-slot"),
    path("slots/update", views.UpdateSlots.as_view(), name="update-slot"),
    path("categories/manage", views.ManageCategoriesView.as_view(), name="manage-categories"),
    path("categories/add", views.AddCategoriesView.as_view(), name="add-categories"),
    path("services/manage", views.ManageServicesView.as_view(), name="manage-services"),
    path("services/add", views.AddServicesView.as_view(), name="add-services"),
    path("services/<int:sid>", views.ServiceView.as_view(), name="view-service"),
    path("account", views.AdminAccountView.as_view(), name="account-settings"),
    path("memberships/manage", views.ManageMembershipsView.as_view(), name="manage-memberships"),
    path("memberships/add", views.AddMembershipsView.as_view(), name="add-memberships"),
    path("beauticians/manage", views.ManageBeauticiansView.as_view(), name="manage-beauticians"),
    path("beauticians/add", views.AddBeauticiansView.as_view(), name="add-beauticians")
]