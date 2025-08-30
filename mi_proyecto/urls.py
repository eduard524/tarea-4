from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('informacion/', include('informacion.urls')),
    path('creditos/', include('creditos.urls')),
]
