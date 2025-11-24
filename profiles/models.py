from django.conf import settings
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name="profile",
            )
    avatar = models.ImageField(
            upload_to="avatars/",
            null=True,
            blank=True,
            help_text="Optional profile picture.",
            )
    description = models.TextField(
            blank=True,
            help_text="Tell people about yourself.",
            )

    def __str__(self):
        return f"{self.user.username}'s profile"

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
