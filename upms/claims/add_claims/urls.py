from django.urls import path
from .           import views

app_name = "upms"

urlpatterns = [

    path('add_claim/', views.Add_Claim, name='add_claim'),
    # path('seearch_members/', views.policy_members, name='policy_members'),


]