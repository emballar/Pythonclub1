from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateField()
    time=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    agenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table='Meeting'

class MeetingMinutes(models.Model):
    meeting=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutes=models.CharField(max_length=255)

    def __str__(self):
        return self.meeting
    
    class Meta:
        db_table='MeetingMinutes'


class Resource(models.Model):
    name=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    url=models.URLField(null=True, blank=True)
    date_entered=models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='Resource'


class Event(models.Model):
    title=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    description=models.TextField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def discountAmount(self):
        self.discount=self.price * .05
        return self.discount
    
    def discountPrice(self):
        disc=self.discountAmount()
        self.discountedPrice=(self.price - disc)


    def __str__(self):
        return self.title
    
    class Meta:
        db_table='Event'
