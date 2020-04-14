from django.db import models

# Create your models here.
class Product(models.Model):  
    product_id = models.AutoField(primary_key=True,auto_created = True)
    product_name = models.CharField(max_length=100)  
    product_sku = models.CharField(max_length=255)
    product_img_url = models.CharField(max_length=100)
    product_unit = models.CharField(max_length=100)
    product_category =  models.CharField(max_length=100)
    product_location = models.CharField(max_length=100)
    manage_stock = models.SmallIntegerField(default=1)
    stock_alert_qty = models.IntegerField()
    product_desc = models.CharField(max_length=100)
    not_for_sale = models.SmallIntegerField(default=0)
    shop_id = models.IntegerField()
    parent_shop_id = models.IntegerField()
    cost_price = models.FloatField()
    sell_price = models.FloatField()
    tax_percentage = models.IntegerField()
    tax_amount = models.FloatField()
    created_dt =  models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100,default='SYSTEM')
    udpated_Dt = models.DateTimeField(auto_now_add=True)  
    updated_by =  models.CharField(max_length=100,default='SYSTEM')
    class Meta:  
        db_table = "product"
