from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import upload_pdf

urlpatterns = [
    path('',upload_pdf),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)