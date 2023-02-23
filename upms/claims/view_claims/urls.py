from django.urls import path
from .           import views

app_name = "upms"

urlpatterns = [

    path('view_claim/', views.View_Claim, name='view_claim'),
    # path('seearch_members/', views.policy_members, name='policy_members'),


]