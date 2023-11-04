from django.db import models
from django.utils import timezone

# Create your models here.

# contact us  model

class Contact(models.Model):

    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=10,null=False)
    question=models.TextField()
    date=models.DateField(default=timezone.now) 



# feed back model

class Feedback(models.Model):

    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,null=False)
    designation=models.TextField(max_length=45,null=False)
    feedback=models.TextField()
    date=models.DateField(default=timezone.now) 

# offer model

class Offer(models.Model):
    contents=models.CharField(max_length=100,null=False)
    date=models.DateField(default=timezone.now) 

# trainer  model

class  Trainer(models.Model):

     trainerid=models.CharField(primary_key=True,max_length=45)
     password=models.CharField(max_length=45)
     name=models.CharField(max_length=30)
     address=models.TextField()
     email=models.EmailField(max_length=45)
     gender=models.CharField(max_length=6)
     phone=models.CharField(max_length=10)
     age=models.IntegerField()
     cityname=models.CharField(max_length=45)
     experience=models.CharField(max_length=45)
     otherdetails=models.TextField()
     trainerpic=models.FileField(max_length=100,upload_to="driving_app/picture",default="")



# PROGRAM MODEL
class Program_details(models.Model):
      program_name=models.CharField(primary_key=True,max_length=50,null=False)
      charges=models.CharField(max_length=50)
      description=models.TextField()




# VEHICLE MODEL


class Vehicle_model(models.Model):
     modelname=models.CharField(primary_key=True, max_length=50,null=False)
     seater=models.CharField(max_length=45,null=False)
     fuel_type=models.CharField(max_length=45)
     vehicle_type=models.CharField(max_length=45)
     other_details=models.TextField()



# VEHICLE DETAIL MODEL

class Vehicle_details(models.Model):
       vehicle_no=models.CharField(primary_key=True,max_length=45)
       color=models.CharField(max_length=45)
       device_no=models.CharField(max_length=45)
       vehicle_model=models.ForeignKey(Vehicle_model,null=False,on_delete=models.DO_NOTHING)
       vehicle_pic=models.FileField(max_length=100,upload_to="driving_app/vehicle_picture",default="")




# TRAINEE MODEL

class Trainee(models.Model):
     
      name=models.CharField(max_length=45,null=False)
      email=models.EmailField(max_length=45,null=False)
      phone=models.CharField(max_length=10,null=False)
      address=models.TextField()
      program=models.ForeignKey(Program_details,null=False,on_delete=models.DO_NOTHING)
      transaction_no=models.CharField(max_length=45)
      trainer=models.OneToOneField(Trainer,null=True,on_delete=models.CASCADE) 
      trainee_id=models.CharField(max_length=45,null=True)
      password=models.CharField(max_length=45,null=True)
      date=models.DateField(default=timezone.now) 
      
      
      


class Ride_log(models.Model):
    vehicle_details=models.ForeignKey(Vehicle_details,null=False,on_delete=models.DO_NOTHING)
    start_point=models.CharField(max_length=45,null=False)
    destination=models.CharField(max_length=45,null=False)
    trainer=models.CharField(max_length=45,null=False)
    trainee=models.CharField(max_length=45,null=False)
    start_time=models.TimeField(default=timezone.now)
    date=models.DateField(default=timezone.now)
    performance=models.TextField()
    











     # employee_type=models.ForeignKey(EmployeeType,null=False,on_delete=models.DO_NOTHING)
