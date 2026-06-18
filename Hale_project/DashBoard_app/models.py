from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Feeback(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField(blank = True)

class ADDSECTION(models.Model):
    id = models.AutoField(primary_key=True )
    sec_date=models.DateField(default=timezone.now)
    sec_duration1=models.TimeField()
    sec_duration2=models.TimeField()
    sec_department=models.CharField(max_length=200)
    sec_op_no=models.IntegerField()
    sec_break1=models.TimeField()
    sec_break2=models.TimeField()
    sec_doctor=models.CharField(max_length=100)
    
class PatientTable(models.Model):
    id = models.AutoField(primary_key=True )
    patient_name=models.CharField(max_length=100)
    patient_age=models.IntegerField()
    patient_gender=models.CharField(max_length=10)
    patient_phone=models.IntegerField()
    patient_address=models.TextField(blank = False)
    patient_discription=models.TextField(blank = True)
    patient_reg_date=models.DateField(default=timezone.now)
    
    

class MedicineList(models.Model):
        medicine_id = models.AutoField(primary_key=True,blank=True,null=False)
        generic_name = models.CharField(max_length=100,default='') 
        category = models.CharField(max_length=50,default='')
        desc1 = models.CharField(max_length=300,default='') 
        desc2 = models.CharField(max_length=3000,default='') 
        exp_date = models.DateField()
        price = models.IntegerField(default=0)
        use = models.CharField(max_length=1000,default="")
        Quantity = models.IntegerField(default=0)   
        def calculate_total_price(self):
            return self.price * self.Quantity
    

class APPOINTMENTSAVED(models.Model):
    id = models.AutoField(primary_key=True)
    app_id=models.IntegerField()
    app_date=models.DateField(default=timezone.now)
    app_Name=models.CharField(max_length=100)
    app_age=models.IntegerField()
    app_gender=models.CharField(max_length=100)
    app_Appointed_doctor=models.CharField(max_length=100)
    app_discription=models.TextField()
    app_op_no=models.IntegerField()
    app_department=models.CharField(max_length=100)
    app_doctor_id=models.IntegerField(null=True)
    app_mark=models.BooleanField(default=False)
    app_doctor_priscription=models.TextField(null=True)
    app_medicine=models.TextField(default=True)
    app_frequency=models.CharField(max_length=100)
    app_startdate=models.DateField(default=timezone.now)
    app_enddate=models.DateField(null=True)
    app_refills_remaining=models.CharField(max_length=100)
    app_dosage=models.CharField(max_length=100,default=True)
    app_Route_0f_administration=models.CharField(max_length=100,default=True)
    app_medicine_priscribed=models.TextField(default=True)
    app_medicine_dosage=models.TextField(default=True)
    app_medicine_duration=models.TextField(default=True)
    app_advice_given=models.TextField(default=True,null=True, blank=True)
    app_fee=models.IntegerField(default="0")
class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_op_nos=models.IntegerField()
    dept_head_of_dept=models.CharField(max_length=100)
    dept_discription=models.TextField(null=True)
    dept_contact=models.IntegerField()
    
class Staffs(models.Model):
     id = models.AutoField(primary_key=True )
     staff_name=models.CharField(max_length=100)
     staff_age=models.IntegerField()
     staff_gender=models.CharField(max_length=20)
     staff_phone_no=models.IntegerField()
     staff_address=models.TextField()
     staff_role=models.CharField(max_length=100)
# id = models.AutoField(primary_key=True, default=2440     
     
class profit(models.Model):
    med_profit=models.IntegerField(default=0)
    patient_profit=models.IntegerField(default=0)
  
