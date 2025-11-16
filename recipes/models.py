from django.conf import settings
from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    instructions = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str___(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("recipe_list")
