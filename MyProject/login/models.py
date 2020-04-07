from django.db import models

# Create your models here.
class Login(models.Model):  
    login_id = models.CharField(max_length=100)  
    password = models.CharField(max_length=100)
    created_date = models.DateField()  
    class Meta:  
        db_table = "login_details"