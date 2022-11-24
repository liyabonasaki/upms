from deprecated import deprecated
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.



@deprecated(version='1.0', reason="moving away from this function --> due to templates")
def policy_members(request):
    return HttpResponse("Manage Policy Members")

def policy_members(request):
    template = loader.get_template('members.html')
    return HttpResponse(template.render())
