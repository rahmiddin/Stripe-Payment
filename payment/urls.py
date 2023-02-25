from django.contrib import admin
from django.urls import path, include
from .views import CreateCheckoutSession, ProductLandingView, CancelView, SuccessView

urlpatterns = [
    path('create-checkout-session/<pk>/', CreateCheckoutSession.as_view(), name='create-checkout-session'),
    path('', ProductLandingView.as_view(), name='landing-page'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel')
]