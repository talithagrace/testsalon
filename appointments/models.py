from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

#add model for hair styles, including field for price starting from
#this needs to appear on the same page as the availability form
#need the booking form to also appear on the front page, use javascript to jump to sections with scroll

# Create your models here.
DAY1 = "Monday"
DAY2 = "Tuesday"
DAY3 = "Wednesday"
DAY4 = "Thursday"
DAY5 = "Friday"
DAY6 = "Saturday"
DAY7 = "Sunday"

TIME1 = "09:00"
TIME2 = "10:00"
TIME3 = "11:00"
TIME4 = "12:00"
TIME5 = "13:00"
TIME6 = "14:00"
TIME7 = "15:00"
TIME8 = "16:00"
TIME9 = "17:00"
TIME10 = "18:00"
TIME11 = "19:00"
TIME12 = "20:00"

class Services(models.Model):
    styles = models.CharField(max_length=30, blank=False, null=True, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='price starts from (£)')

    def add(self):
        self.save()

    def __str__(self):
        return '%s %s' % (self.styles, self.price)
        #currency = '£'
        #return '%s %s %s' % (self.styles, currency.replace(" ",""), self.price)

class Day(models.Model):
    DAY_CHOICES = (
        (DAY1, "Mon"),
        (DAY2, "Tue"),
        (DAY3, "Wed"),
        (DAY4, "Thu"),
        (DAY5, "Fri"),
        (DAY6, "Sat"),
        (DAY7, "Sun"),
    )
    day = models.CharField(max_length=14, choices=DAY_CHOICES, default=DAY1)

    def add(self):
        self.save()
    #date = models.DateField(blank=False, null=True) #use this instead of days above potentially
    def __str__(self):
        return self.day

class Availability(models.Model):
    week_commencing = models.DateField(blank=False, null=True)
    week_day = models.ForeignKey(Day, on_delete=models.CASCADE, default="")
    TIME_CHOICES = (
        (TIME1, "09:00"),
        (TIME2, "10:00"),
        (TIME3, "11:00"),
        (TIME4, "12:00"),
        (TIME5, "13:00"),
        (TIME6, "14:00"),
        (TIME7, "15:00"),
        (TIME8, "16:00"),
        (TIME9, "17:00"),
        (TIME10, "18:00"),
        (TIME11, "19:00"),
        (TIME12, "20:00"),
    )
    time = models.CharField(max_length=8, choices=TIME_CHOICES, default=TIME1)
    class Meta:
        unique_together = ("week_day", "time", "week_commencing") #only one timeslot choice per date allowed

    def add(self):
        self.save()

    def __str__(self):
        return '%s %s %s' % (self.week_commencing, self.week_day, self.time)

class HairAppointment(models.Model):
    user = models.ForeignKey('auth.User')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(verbose_name='phone', max_length=15, validators=[phone_regex], blank=False, null=True) #validators need to be in a list hence[]
    email = models.EmailField(blank=False, null=True)
    #timeslot = models.ForeignKey(Availability, on_delete=models.CASCADE, default="", unique=True)
    timeslot = models.OneToOneField(Availability, on_delete=models.CASCADE) #onetoone means this slot will only be available once
    #style = models.CharField(max_length=200)
    style = models.ForeignKey(Services, on_delete=models.CASCADE)

    def add(self):
        self.save()

    def __str__(self):
        return '%s %s' % (self.timeslot, self.style)
