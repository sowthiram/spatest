from django.urls import path
from owner import views


urlpatterns=[
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("slots/add", views.AddTimeslotsView.as_view(), name="add-timeslots"),
    path("slots/manage", views.ManageTimeslotsView.as_view(), name="manage-timeslots"),
    path("categories/manage", views.ManageCategoriesView.as_view(), name="manage-categories"),
    path("categories/add", views.AddCategoriesView.as_view(), name="add-categories"),
    path("categories/<int:cid>/delete", views.DeleteCategoriesView.as_view(), name="delete-categories"),
    path("services/manage", views.ManageServicesView.as_view(), name="manage-services"),
    path("services/add", views.AddServicesView.as_view(), name="add-services"),
    path("services/<int:sid>/delete", views.DeleteServicesView.as_view(), name="delete-services"),
    path("services/<int:sid>", views.ServiceView.as_view(), name="view-service"),
    path("account", views.AdminAccountView.as_view(), name="account-settings"),
    path("memberships/manage", views.ManageMembershipsView.as_view(), name="manage-memberships"),
    path("memberships/add", views.AddMembershipsView.as_view(), name="add-memberships"),
    path("memberships/<int:mid>/delete", views.DeleteMembershipView.as_view(), name="delete-memberships"),
    path("beauticians/manage", views.ManageBeauticiansView.as_view(), name="manage-beauticians"),
    path("beauticians/add", views.AddBeauticiansView.as_view(), name="add-beauticians"),
    path("beauticians/<int:bid>/delete", views.DeleteBeauticianView.as_view(), name="delete-beauticians"),
    path("memberships/<int:mid>", views.DetailMembershipView.as_view(), name="membership-view"),
    path("timeslots/manage", views.ManageTimeslotsView.as_view(), name="manage-timeslots"),
    path("timeslots/add", views.AddTimeslotsView.as_view(), name="add-timeslots"),
    path("timeslots/<int:tid>/delete", views.DeleteTimeslotsView.as_view(), name="delete-timeslots"),
    path("beauticians/<int:bid>", views.DetailBeauticianView.as_view(), name="beautician-view"),
    path("categories/<int:cid>", views.DetailCategoryView.as_view(), name="view-category"),
    path("memberships/<int:mid>/update", views.UpdateMembershipView.as_view(), name="update-membership"),
    path("services/<int:sid>/update", views.UpdateServiceView.as_view(), name="update-service")



]