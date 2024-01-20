from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Feeback(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField(blank = True)

class ADDSECTION(models.Model):
    sec_date=models.DateField(default=timezone.now)
    sec_duration1=models.TimeField()
    sec_duration2=models.TimeField()
    sec_department=models.CharField(max_length=200)
    sec_op_no=models.IntegerField()
    sec_break1=models.TimeField()
    sec_break2=models.TimeField()
    sec_doctor=models.CharField(max_length=100)
    
class PatientTable(models.Model):
    patient_name=models.CharField(max_length=100)
    patient_age=models.IntegerField()
    patient_gender=models.CharField(max_length=10)
    patient_phone=models.IntegerField()
    patient_address=models.TextField(blank = False)
    patient_discription=models.TextField(blank = True)
    patient_reg_date=models.DateField(default=timezone.now)
    
    

class APPOINTMENTSAVED(models.Model):
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





class ProductList(models.Model):
        product_id = models.AutoField(primary_key=True,blank=True,null=False)
        product_name = models.CharField(max_length=100,default='') 
        category = models.CharField(max_length=50,default='')
        desc1 = models.CharField(max_length=300,default='') 
        desc2 = models.CharField(max_length=3000,default='') 
        exp_date = models.DateField()
        price = models.IntegerField(default=0)
        image = models.ImageField(upload_to="user/images",default="")
        discount = models.IntegerField(default=0)
        features = models.CharField(max_length=1000,default="")
        use = models.CharField(max_length=1000,default="")
        Quantity = models.IntegerField(default=0)   

    
