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
    path("packages/manage", views.ManagePackagesView.as_view(), name="manage-packages"),
    path("packages/add", views.AddPackagesView.as_view(), name="add-packages"),
    path("beauticians/<int:bid>", views.DetailBeauticianView.as_view(), name="beautician-view"),
    path("categories/<int:cid>", views.DetailCategoryView.as_view(), name="view-category"),
    path("bookings/manage", views.ManageBookingsView.as_view(), name="manage-bookings"),
    path("memberships/<int:mid>/update", views.UpdateMembershipView.as_view(), name="update-membership"),
    path("services/<int:sid>/update", views.UpdateServiceView.as_view(), name="update-service"),
    path("categories/<int:cid>/update", views.UpdateCategoryView.as_view(), name="update-category"),
    path("beautician/<int:bid>/update", views.UpdateBeauticianView.as_view(), name="update-beautician"),
    path("timeslot/<int:tid>/update", views.UpdateTimeslotView.as_view(), name="update-timeslot"),
    path("package/<int:pid>/update", views.UpdatePackageView.as_view(), name="update-package"),
    path("package/<int:pid>", views.DetailPackageView.as_view(), name="view-package"),
    path("package/<int:pid>/delete", views.DeletePackageView.as_view(), name="delete-package"),
    path("giftcards/manage", views.ManageGiftCardsView.as_view(), name="manage-giftcards"),
    path("giftcards/add", views.AddGiftCardsView.as_view(), name="add-giftcards"),
    path("giftcard/<int:gid>", views.DetailGiftCardView.as_view(), name="view-giftcard"),
    path("giftcards/<int:gid>/update", views.UpdateGiftCardView.as_view(), name="update-giftcard"),
    path("giftcards/<int:gid>/delete", views.DeleteGiftCardView.as_view(), name="delete-giftcard"),














]