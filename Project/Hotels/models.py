from django.db import models
from .modelsTwo import *


class Region(models.Model):
    name = models.CharField(max_length=50)  

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)  
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')  # Связь с регионом

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)  
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')  # Связь с городом

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')  # Связь с отелем
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type} в {self.hotel.name}"


class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='bookings')
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name='booking')  # 1:1 связь с номером
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Бронирование {self.room} гостем {self.guest}"


class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')  # 1:1 связь с бронированием
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50, default='Completed')

    def __str__(self):
        return f"Платёж {self.amount_paid} за {self.booking}"
