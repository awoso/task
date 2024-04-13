from uuid import uuid4
from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.

class EVENT(models.Model):
    CONCERT = 'C'
    CONFERENCE = 'C'
    GAMES = 'G'
    BOOK_CHOICE = [
        (CONCERT, 'concert'),
        (CONFERENCE, 'conference'),
        (GAMES, 'games'),
    ]
    name = models.CharField(max_length=255)
    summary = models.TextField()
    event_description = models.CharField('ISBN', max_length=255)
    attendees = models.CharField('Genre', max_length=8, choices=BOOK_CHOICE, default=CONFERENCE)
    email = models.CharField('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.name}"

    def __str__(self):
        return f"{self.title} {self.event_description}"

    def __str__(self):
        return f"{self.title} {self.attendees}"

    def __str__(self):
        return f"{self.title} {self.email}"



class Customer(models.Model):
    name = models.CharField('Name', max_length=255)
    email = models.CharField('Author', max_length=255)
    password = models.CharField('Password', max_length=255)

    def __str__(self):
        return f"{self.title} {self.name}"

    def __str__(self):
        return f"{self.title} {self.email}"

    def __str__(self):
        return f"{self.title} {self.password}"



class Ticket(models.Model):
    name = models.CharField('Name', max_length=255)
    reservation_number = models.CharField('Reservation Number', max_length=255)
    ticket_quantity = models.IntegerField('Ticket Quantity')
    reservation_date = models.DateField('Reservation Date')

    def __str__(self):
        return f"{self.name} - {self.reservation_number}"

    def __str__(self):
        return f"{self.name} - {self.name}"

    def __str__(self):
        return f"{self.name} - {self.reservation_date}"

    def __str__(self):
        return f"{self.name} - {self.ticket_quantity}"
