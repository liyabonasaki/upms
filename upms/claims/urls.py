from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('menu/', include('upms.system.menu.urls')),
    # path('register/', include('register.urls')),
    path('add_claims/', include('claims.add_claims.urls')),
    # path('search_claims/' , include('claims.search_claims.urls')),
    # path('update/' , include('claims.update.urls')),
    path('view_claims/' , include('claims.view_claims.urls')),

]
