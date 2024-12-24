from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apl/', include('main1.urls')),
    path('', lambda request: redirect('/apl/')),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
