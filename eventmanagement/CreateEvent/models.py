from django.db import models
from account.models import Teacher, Student


# Create your models here.

class Event(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    teacher = models.ManyToManyField('account.Teacher')
    attendees = models.ManyToManyField('account.Student', through="AttendEvent")
    EventId = models.AutoField(primary_key=True)
    EventTitle = models.CharField(max_length=120)
    DateOfEvent = models.DateField()
    MaxParticipants = models.IntegerField()


class Room(models.Model):
    RoomId = models.AutoField(primary_key=True)
    RoomName = models.CharField(max_length=120)


class AttendEvent(models.Model):
    status_type = (('JOINED', 'ATTENDING'),('NOT JOINED', 'NOT ATTENDING'))
    student = models.ForeignKey('account.Student', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=status_type, default='JOINED')




