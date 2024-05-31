from django.contrib import admin
from django.urls import path, include
import corretor_ia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('corretor_ia.urls'))
]
