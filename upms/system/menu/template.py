

def path(class_name):
    templates_map = {
        'AdminView' : ['system/menu/home.html', 'ADM-1'],

    }

    return  templates_map[class_name]