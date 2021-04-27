from django.db import models
from django.conf import settings


# Create your models here.

class Room(models.Model):
    ROOM_CATEGORIES = (
        ('KIN', 'KING'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('SIN', 'SINGLE')

    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'room {self.number}  {self.category} {self.beds} beds {self.capacity} guests'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} since {self.check_in} till {self.check_out}'

