from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('bookings/', views.bookings, name="bookings"),
]
