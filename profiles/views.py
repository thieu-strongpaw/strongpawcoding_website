from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView
from django.shortcuts import get_object_or_404

from .models import Profile
from .forms import ProfileForm

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profile_detail.html"

class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class MyProfileView(LoginRequiredMixin, DetailView):
    """
    Convenience view: /profile/me/ shows the current user's profile
    without needing pk in URL.
    """
    model = Profile
    template_name = "profile_detail.html"
    
    def get_object(self):
        return self.request.user.profile

