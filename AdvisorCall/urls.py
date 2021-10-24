from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('api/', include('AdvisorCall.API.urls')),

]