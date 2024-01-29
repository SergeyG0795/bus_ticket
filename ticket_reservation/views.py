from datetime import datetime

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect

from ticket_reservation.models import Ticket, Bus


def schedule(request):
    current_time = datetime.now()
    buses = Bus.objects.filter(departure_time__gt=current_time)
    context = {'buses': buses}
    return render(request, 'reserve_tickets/schedule.html', context)


@login_required
def reserve_ticket(request, bus_id):
    bus = get_object_or_404(Bus, pk=bus_id)

    if request.method == 'POST' and bus.available_seats >= 0:
        bus.available_seats -= 1
        bus.save()
        user = request.user
        ticket = Ticket.objects.create(user=user, bus=bus, ticket_price=bus.price)
        return render(
            request,
            'reserve_tickets/reserve_confirmation.html',
            {'ticket': ticket}
        )

    return render(
        request,
        'reserve_tickets/reserve_ticket.html',
        {'bus': bus, 'messages': 'Нет свободных мест'}
    )


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Здесь передается объект запроса и объект пользователя
            return redirect('profile')
    else:
        form = AuthenticationForm(request)
    return render(request, 'auth/login_form.html', {'form': form})