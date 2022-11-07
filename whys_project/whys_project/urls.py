from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ukol/', include('ukol.urls')),
    path('admin/', admin.site.urls),
]
