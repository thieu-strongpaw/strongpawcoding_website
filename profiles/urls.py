from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView, MyProfileView

urlpatterns = [
        path("me/", MyProfileView.as_view(), name="my_profile"),
        path("<int:pk>", ProfileDetailView.as_view(), name="profile_detail"),
        path("<int:pk>/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
        ]
