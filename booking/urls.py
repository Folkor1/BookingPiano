from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('bookings/', views.BookingsView.as_view(), name="bookings"),
    path('manage_bookings/', views.ManageBookingsView.as_view(), name='manage_bookings'),
    path('success/', views.success, name="success"),
    path('edit/<booking_id>', views.edit_booking_date, name="edit"),
]
