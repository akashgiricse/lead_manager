from django.urls import path, include


urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('leads.urls')),
]
