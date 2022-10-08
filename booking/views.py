from django.shortcuts import render
from django.views import generic
from .models import About

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


def bookings(request):
    """
    Render bookings page
    """
    return render(request, "bookings.html")
