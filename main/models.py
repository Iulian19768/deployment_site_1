from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Booking (models. Model):
    nume =models. CharField(max_length=100)
    numar_tel =models. IntegerField()
    email =models. CharField(max_length=100)
    date =models. CharField(max_length=100)
    time =models. CharField(max_length=100)
    country =models. CharField(max_length=100)
    city =models. CharField(max_length=100)
    age =models. CharField(max_length=100, default='0')
    insta_handler =models. CharField(max_length=100, default='SOME STRING')
    how_much_per_month =models. CharField(max_length=100, default='0')
    how_much_wish =models. CharField(max_length=100, default='SOME STRING')
    obstacle =models. CharField(max_length=100, default='SOME STRING')
    how_much_invest =models. CharField(max_length=100, default='0')
    


    def __str__(self):
        return self.nume