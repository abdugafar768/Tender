from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('dj_rest_auth.urls')),
    path('account/registration/', include('dj_rest_auth.registration.urls')),
    
    path('tender/',include('tender.urls')),
    
]
