def path(class_name):
    templates_map = {
        'policy_members' : ['upms/templates/members/members.html'],
    }
    return templates_map[class_name]