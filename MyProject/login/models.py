from django.db import models

# Create your models here.
class Login(models.Model):  
    user_id = models.AutoField(primary_key=True,auto_created = True)
    user_name = models.CharField(max_length=100)  
    password = models.CharField(max_length=255)
    user_role = models.CharField(max_length=100)
    active_flag = models.IntegerField(default=1)
    shop_id = models.IntegerField()
    parent_shop_id = models.IntegerField()
    last_loggedin = models.DateTimeField(auto_now_add=True)
    last_logggedout = models.DateTimeField(auto_now_add=True)
    created_dt =  models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100,default='SYSTEM')
    updated_dt = models.DateTimeField(auto_now_add=True)  
    updated_by =  models.CharField(max_length=100,default='SYSTEM')
    class Meta:  
        db_table = "user_login"