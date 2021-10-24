from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('advisor', views.AdvisorViewSet, basename='advisor')

urlpatterns = [
    path('user/', views.User_All),
    path('user/register/', views.User_create),

    path('', include(router.urls)),

]