from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

#media(image) url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AdvisorCall.urls')),
    # path('api/', include('AdvisorCall.API.urls')),

    #api auth
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
