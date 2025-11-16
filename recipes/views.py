from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

from .models import Recipe
from .forms import CommentForm


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipe_list.html"


class CommentGet(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Recipe
    form_class = CommentForm
    template_name = "recipe_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.recipe = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        recipe = self. object
        return reverse("recipe_detail", kwargs={"pk": recipe.pk})


class RecipeDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = (
        "title",
        "instructions",
    )
    template_name = "recipe_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = "recipe_delete.html"
    success_url = reverse_lazy("recipe_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe_new.html"
    fields = (
        "title",
        "ingredients",
        "instructions",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
