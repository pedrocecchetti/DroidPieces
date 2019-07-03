from django.contrib import admin
from django.urls import path, include

from core.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
