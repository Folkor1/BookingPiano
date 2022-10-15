from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from .models import About, Bookings
from django.http import HttpResponseRedirect



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
            context = {'lesson': lesson, 'lesson_type': lesson_type, 'date': date, 'time': time, 'status': status}
            return HttpResponseRedirect(reverse('success'), context)


class ManageBookingsView(generic.ListView):
    """
    Render manage bookings page
    """
    model = Bookings
    template_name = "manage_bookings.html"


def success(request):
    """
    Render success page
    """
    return render(request, "success.html")


def edit_booking_date(request, booking_id):
    """
    Edit booking date and time
    """
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == 'POST':
        booking.date = request.POST.get('edit_date_inp')
        booking.time = request.POST.get('edit_time_inp')
        booking.save()
    return render(request, 'edit_booking_date.html')
