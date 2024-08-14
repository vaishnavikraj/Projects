from django.db import models

class register(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    
class station(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    longitude = models.CharField(max_length=150)
    latitude = models.CharField(max_length=150)
    slot = models.CharField(max_length=150)    
    
class location(models.Model):
    locations = models.CharField(max_length=150)     
    
    
    
class feedback(models.Model):
    user_id = models.CharField(max_length=150)                  
    feedbacks = models.CharField(max_length=150)                  
    
class complaint(models.Model):
    user_id = models.CharField(max_length=150)                  
    complaints = models.CharField(max_length=150)     
    
class booking(models.Model):
    station_id = models.CharField(max_length=150)
    user_id = models.CharField(max_length=150)
    station_name = models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    time_slot = models.CharField(max_length=150)
    charging_slot = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    status = models.CharField(max_length=150)     



class payment(models.Model):
    id = models.IntegerField(primary_key = True)
    user_id=models.CharField(max_length=150)
    month=models.CharField(max_length=150)
    slot=models.CharField(max_length=150)
    amount=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    payment_type=models.CharField(max_length=150)
    card_no=models.CharField(max_length=150)
    cvv=models.CharField(max_length=150)
    cardname=models.CharField(max_length=150)
    