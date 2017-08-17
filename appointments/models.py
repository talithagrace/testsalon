from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
class HairAppointment(models.Model):
    user = models.ForeignKey('auth.User')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(verbose_name='phone', max_length=15, validators=[phone_regex], blank=False, null=True) #validators need to be in a list hence[]
    email = models.EmailField(blank=False, null=True)
    date = models.DateField(blank=False, null=True)
    AM1 = "09:00"
    AM2 = "11:00"
    PM1 = "13:00"
    PM2 = "15:00"
    TIMESLOT_CHOICES = (
        (AM1, "09:00"),
        (AM2, "11:00"),
        (PM1, "13:00"),
        (PM2, "15:00"),
    )
    timeslot = models.CharField(max_length=25, choices=TIMESLOT_CHOICES, default=AM1)
    style = models.CharField(max_length=200)
    class Meta:
        unique_together = ("date", "timeslot") #only one timeslot choice per date allowed

    def add(self):
        self.save()
