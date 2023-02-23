from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('menu/', include('upms.system.menu.urls')),
    # path('register/', include('register.urls')),
    path('/', include('upms.authentication.urls')),
    path('upms/members/', include('upms.members.urls')),
    path('upms/claims/' , include('upms.claims.urls'))

]
