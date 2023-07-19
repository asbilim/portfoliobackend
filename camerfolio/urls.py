from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/',include('jet.urls')),
    path('dashboard/',include('jet.dashboard.urls','jet-dashboard')),
    path('',include('api.urls'))
]
