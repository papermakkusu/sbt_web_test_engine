from django.conf.urls import include, url
from django.contrib import admin
from front_end import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('front_face.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)