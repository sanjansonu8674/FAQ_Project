from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet  # Import the FAQViewSet from your views

# Create a router and register the FAQViewSet
router = DefaultRouter()
router.register(r'faqs', FAQViewSet)  # Register the FAQViewSet under the 'faqs' endpoint

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include all router URLs
]