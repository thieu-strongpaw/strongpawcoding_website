from django.contrib import admin
from .models import Recipe, Comment


class CommentInline(admin.StackedInline):
    model = Comment


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "title",
        "instructions",
        "author",
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)
