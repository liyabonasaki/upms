from django.urls          import path

from upms.system.menu.views import AdminView

url_patterns = [
    path('admin/' , AdminView.as_view(),  name='admin')
]