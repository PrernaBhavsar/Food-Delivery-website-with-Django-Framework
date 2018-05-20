from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser


mumbai='Mumbai'
delhi='Delhi'
kolkata='Kolkata'
bengaluru='Bengaluru'

CITY_CHOICES=(
    (mumbai,'Mumbai'),
    (delhi, 'Delhi'),
    (kolkata, 'Kolkata'),
    (bengaluru,'Bengaluru'),

)

ORDER_MENU=(
    ('Smoked Chipotle Rice','Smoked Chipotle Rice'),
    ('Baked Beans with Vegetables','Baked Beans with Vegetables'),
    ('Simple italian pizza with cherry tomatoes','Simple italian pizza with cherry tomatoes'),
    ('Autumn pumpkin soup','Autumn pumpkin soup'),
    ('Caesar Salad','Caesar Salad'),
    ('Granola with cherries and strawberries','Granola with cherries and strawberries'),
    ('Black Bean Tacos With Olives','Black Bean Tacos With Olives'),
    ('Hummus and Pita bread','Hummus and Pita bread'),
    ('Lentil and Charred Broccoli Chaat','Lentil and Charred Broccoli Chaat'),
    ('Blue Corn Breakfast Tacos With Scrambled Eggs','Blue Corn Breakfast Tacos With Scrambled Eggs'),

)

class Signup(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=20)
    address = models.TextField(max_length=200)
    city= models.CharField(max_length=100,choices=CITY_CHOICES, null=True)
    pin=models.BigIntegerField()
    plan=models.CharField(max_length=100, null=True)
    order=models.CharField(max_length=100,choices=ORDER_MENU, null=True)
    total=models.FloatField(null=True)
    def __str__(self):
        return '{}  {}  {}'.format(self.first_name, self.city, self.plan)





