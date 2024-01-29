from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class City(models.Model):
    city_name = models.CharField(max_length=100, blank=False, unique=True, verbose_name='Город')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.city_name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Bus(models.Model):
    bus_name = models.CharField(max_length=100, unique=True, blank=False, default="")
    available_seats = models.SmallIntegerField(blank=False, default=0)
    from_city = models.ForeignKey(City, on_delete=CASCADE, blank=False, related_name='routes_from')
    to_city = models.ForeignKey(City, on_delete=CASCADE, blank=False, related_name='routes_to')
    departure_time = models.DateTimeField(blank=False, null=False)
    arrival_time = models.DateTimeField(blank=False, null=False)
    price = models.FloatField(default=0, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.bus_name}: {self.from_city.city_name}-{self.to_city.city_name}'

    class Meta:
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобусы'


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, blank=False)
    bus = models.ForeignKey(Bus, on_delete=CASCADE, blank=False)
    ticket_price = models.FloatField(default=0, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}-{self.user.username} {self.bus.from_city.city_name}-{self.bus.to_city.city_name}'
