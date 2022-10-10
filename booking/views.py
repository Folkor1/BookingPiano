from django.shortcuts import render
from django.views import generic
from .models import About, Bookings

def homepage(request):
    """
    Render the home page
    """
    return render(request, "index.html")


class AboutView(generic.ListView):
    """
    Render about page
    """
    model = About
    template_name = "about.html"


class BookingsView(generic.ListView):
    """
    Render bookings page
    """
    model = Bookings
    template_name = "bookings.html"
