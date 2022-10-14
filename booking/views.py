from django.shortcuts import render, redirect
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

    def post(self, request):
        if request.method == 'POST':
            lesson = request.POST.get('lesson_inp')
            lesson_type = request.POST.get('lesson_type_inp')
            date = request.POST.get('date_inp')
            time = request.POST.get('time_inp')
            status = True
            booking = Bookings(lesson=lesson, lesson_type=lesson_type, date=date, time=time, status=status)
            booking.save()
            return redirect('manage_bookings')


def manage_bookings(request):
    """
    Render manage bookings page
    """
    return render(request, "manage_bookings.html")
