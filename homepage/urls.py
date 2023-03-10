from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'homepage'

urlpatterns = [
    path('',views.IndexView, name='homepage_url'),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)