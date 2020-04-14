from django.db import models

# Create your models here.
class Product(models.Model):  
    product_id = models.AutoField(primary_key=True,auto_created = True)
    product_name = models.CharField(max_length=100)  
    product_sku = models.CharField(max_length=255)
    product_img_url = models.CharField(max_length=100)
    product_unit = models.IntegerField(default=1)
    product_category = models.IntegerField()
    product_img_url = models.CharField(max_length=100)
    product_unit = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    product_location = models.CharField(max_length=100)
    manage_stock = models.IntegerField(default=1)
    stock_alert_qty = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=100)
    not_for_sale = models.IntegerField(default=0)
    shop_id = models.CharField(max_length=100)
    parent_shop_id = models.CharField(max_length=100)
    cost_price = models.IntegerField()
    sell_price = models.CharField(max_length=100)
    tax_percentage = models.CharField(max_length=100)
    tax_amount = models.FloatField()
    created_dt =  models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100,default='SYSTEM')
    updated_dt = models.DateTimeField(auto_now_add=True)  
    updated_by =  models.CharField(max_length=100,default='SYSTEM')
    class Meta:  
        db_table = "product"
