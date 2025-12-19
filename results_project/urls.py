from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('django-admin/', admin.site.urls),

    # Admin app (public link generation)
    path('', include('adminapp.urls')),

    # Student result search
    path('results/', include('studentapp.urls')),
]

# Serve media files even when DEBUG=False (Render)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
