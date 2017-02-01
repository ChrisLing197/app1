from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from decimal import Decimal

# User model
class Registration(models.Model):
    BUYER = "BU"
    SELLER = "SE"
    ADMIN = "AD"

    ROLE_TYPE_CHOICES = (
            (SELLER, "Seller"),
            (BUYER, "Buyer"),
            (ADMIN, "Admin")
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctors = models.ManyToManyField('self',
            related_name="patients",
            limit_choices_to={'role': SELLER})

    role = models.CharField(
            max_length=2,
            choices=ROLE_TYPE_CHOICES,
            default=BUYER
        )

    date_registered = models.DateField(auto_now=True)
    date_of_birth   = models.DateField(blank=True,null=True)
    phone_number    = models.CharField(max_length=10,blank=True,null=True)
    mail_address    = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.user.username

# Data Models

class Appointment(models.Model):
    buyer = models.ForeignKey("Registration",
            limit_choices_to={'role': Registration.BUYER},
            related_name="appointments_buyer"
        )
    seller = models.ForeignKey("Registration",
            limit_choices_to={'role': Registration.SELLER},
            related_name="appointments_seller"
        )

    date_created = models.DateTimeField(auto_now=True)
    date_scheduled = models.DateTimeField()

    def __str__(self):
        return "["+self.date_scheduled.isoformat()+"]"+self.doctor

class Activity(models.Model):
    REGISTRATION = "RG"
    APPOINTMENT = "AP"
    PRESCRIPTION = "PS"
    RECORD = "RC"
    LOGIN = "LG"

    ACTIVITY_TYPE_CHOICES = (
            (REGISTRATION,"Registration"),
            (APPOINTMENT,"Appointment"),
            (PRESCRIPTION,"Prescription"),
            (RECORD,"Record"),
            (LOGIN,"Login"),
        )
    
    activity_type = models.CharField(
                max_length=2,
                choices=ACTIVITY_TYPE_CHOICES
            )
    timestamp = models.DateTimeField(auto_now=True)
    user_responsible = models.ForeignKey("Registration")
    description = models.TextField()

    def __str__(self):
        return "["+self.timestamp.isoformat()+"] "+str(self.user_responsible)+"|"+self.activity_type+"-"+self.description

class Message(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey("Registration",
            related_name="sent_messages")
    recipient = models.ForeignKey("Registration",
            related_name="received_messages")
    text = models.TextField()

    def __str__(self):
        return "["+self.timestamp.isoformat()+"]"+str(self.sender)+"|"+str(self.recipient)

class Item(models.Model):
    timestamp=models.DateTimeField(auto_now=True)
    poster=models.ForeignKey(User,related_name="posted_item",null=True)
    user=User
    name=models.CharField(max_length=32,blank=True,null=True)
    description=models.TextField()

    ChOiC=(
        ('NE','New'),
        ('NM','Near Mint or Better'),
        ('UP','Used or Pre-owned'),
        ('LU','Lightly Used'),
        ('MU','Moderately Used'),
        ('NS','Not Specified')
    )
    condition=models.CharField(max_length=2,default='NM',choices=ChOiC)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    quantity=models.PositiveSmallIntegerField(default=1,blank=True,null=True)

    def __str__(self):
        return "["+self.timestamp.isoformat()+"]"+str(self.name)

class Cart(models.Model):
    timestamp=models.DateTimeField(auto_now=True)
    buyer=models.ForeignKey(User,related_name="claimed_item",null=True)
    user=User
    name=models.CharField(max_length=32,blank=True,null=True)
    description=models.TextField()

    ChOiC=(
        ('NE','New'),
        ('NM','Near Mint or Better'),
        ('UP','Used or Pre-owned'),
        ('LU','Lightly Used'),
        ('MU','Moderately Used'),
        ('NS','Not Specified')
    )
    condition=models.CharField(max_length=2,default='NM',choices=ChOiC)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    quantity=models.PositiveSmallIntegerField(default=1,blank=True,null=True)
                                                                 
    def __str__(self):
        return "["+self.timestamp.isoformat()+"]"+str(self.name)
