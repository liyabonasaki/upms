from deprecated                                                import deprecated
from django.http                                               import HttpResponse
from django.template                                           import loader
from upms.members.models import Members


# class PolicyMembers
@deprecated(version='1.0', reason="moving away from this function --> due to templates")
def policy_members(request):
    return HttpResponse("Manage Policy Members")


def policy_members(request):
    members = Members.objects.all().values()
    template = loader.get_template('members.html')

    context = {
        'members' : members,
    }
    return HttpResponse(template.render(context, request))

# def update_members()
