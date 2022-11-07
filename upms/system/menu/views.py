from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic       import TemplateView

from .                          import template


class AdminView(LoginRequiredMixin,  TemplateView):
    template_name, userlevel_needed = template.path('AdminView')