from django.urls import path
from .           import views

app_name = "members"

urlpatterns = [
    path('', views.policy_members, name='policy_members'),
]