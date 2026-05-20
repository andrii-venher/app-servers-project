from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Forward all 'catalog/' URLs to the app's URL configuration
    path('catalog/', include('catalog.urls')),
    # Django site authentication URLs (login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
    # Redirect the root URL to the catalog app
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)