from django.urls import path
from .           import views

app_name = "members"

urlpatterns = [

    path('view_members/', views.policy_members, name='policy_members'),
    # path('seearch_members/', views.policy_members, name='policy_members'),


]