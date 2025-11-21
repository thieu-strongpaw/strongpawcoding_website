from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Template view of the home page"""
    template_name = "home.html"
