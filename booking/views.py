from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic
from .models import About, Bookings
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime


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
        """
        Create new booking
        """
        if request.method == 'POST':
            lesson = request.POST.get('lesson_inp')
            lesson_type = request.POST.get('lesson_type_inp')
            date = request.POST.get('date_inp')
            time = request.POST.get('time_inp')
            status = True
            booking = Bookings(lesson=lesson, lesson_type=lesson_type, date=date, time=time, status=status)
            booking.save()
            messages.success(request, 'Booking successfully added.')
            return HttpResponseRedirect(reverse('manage_bookings'))


class ManageBookingsView(generic.ListView):
    """
    Render manage bookings page
    """
    model = Bookings
    booking = Bookings.objects.all()
    Bookings.check_status(booking)
    template_name = "manage_bookings.html"


def edit_booking_date(request, booking_id):
    """
    Edit booking date and time
    """
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == 'POST':
        booking.date = request.POST.get('edit_date_inp')
        booking.time = request.POST.get('edit_time_inp')
        booking.save()
        messages.success(request, 'Date successfully changed.')
        return redirect('manage_bookings')
    context = {
        'edit_date_lesson': Bookings.get_lesson(booking),
        'edit_date_lesson_type': Bookings.get_lesson_type(booking)
        }
    return render(request, 'edit_booking_date.html', context)


def edit_booking_type(request, booking_id):
    """
    Edit lesson type
    """
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == 'POST':
        booking.lesson_type = request.POST.get('edit_lesson_type')
        booking.save()
        messages.success(request, 'Lesson type successfully changed.')
        return redirect('manage_bookings')
    context = {
        'edit_date_lesson_type': Bookings.get_lesson_type(booking)
        }
    return render(request, 'edit_booking_type.html', context)


def cancel_booking(request, booking_id):
    """
    Cancel booking
    """
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Lesson successfully canceled.')
        return redirect('manage_bookings')
    context = {
        'cancel_lesson': Bookings.get_lesson(booking),
        'cancel_lesson_type': Bookings.get_lesson_type(booking),
        'cancel_date': Bookings.get_date(booking),
        'cancel_time': Bookings.get_time(booking)
        }
    return render(request, 'cancel_booking.html', context)
