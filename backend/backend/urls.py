# Import necessary modules from Django and Django REST Framework
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import the viewsets from the users module
from users.views import UserReadViewSet, UserWriteViewSet, ProfileReadViewSet, ProfileWriteViewSet

# Create a default router for the API endpoints
router = DefaultRouter()

# Register the viewsets with the router
# Each viewset is given a route (e.g. 'users-read') and a basename
router.register(r'users-read', UserReadViewSet, basename='users-read')
router.register(r'users-write', UserWriteViewSet, basename='users-write')
router.register(r'profiles-read', ProfileReadViewSet, basename='profiles-read')
router.register(r'profiles-write', ProfileWriteViewSet, basename='profiles-write')

# Define the URL patterns for the Django application
# This includes the admin site, the API (using the router), and the OAuth2 provider
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin site
    path('api/', include(router.urls)),  # API endpoints
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # OAuth2 provider
]
