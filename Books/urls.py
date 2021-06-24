from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from Books.views import page_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('book.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('404', page_404),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
