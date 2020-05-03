from django.db import models

# Create your models here.
class Product(models.Model):  
    product_id = models.AutoField(primary_key=True,auto_created = True)
    product_name = models.CharField(max_length=100)  
    product_sku = models.CharField(max_length=255, null=True, blank=True)
    product_img_url = models.CharField(max_length=100, null=True, blank=True)
    product_unit = models.CharField(max_length=100)
    product_category =  models.CharField(max_length=100, null=True, blank=True)
    product_brand =  models.CharField(max_length=100, null=True, blank=True)
    product_weight =  models.CharField(max_length=100, null=True, blank=True)
    product_type =  models.CharField(max_length=100, null=True, blank=True)
    product_location = models.CharField(max_length=100, null=True, blank=True)
    manage_stock = models.SmallIntegerField(default=1)
    stock_alert_qty = models.IntegerField()
    product_desc = models.CharField(max_length=100, null=True, blank=True)
    not_for_sale = models.SmallIntegerField(default=0)
    active_flag =  models.CharField(max_length=100,default='1')
    shop_id = models.IntegerField()
    parent_shop_id = models.IntegerField()
    tax_type = models.CharField(max_length=100)
    tax_amount = models.FloatField()
    cost_price_w_tax = models.FloatField()
    cost_price_wo_tax = models.FloatField()
    sell_price = models.FloatField()
    selling_price_tax_type =  models.CharField(max_length=100,default='')
    selling_price_tax_amount = models.FloatField(default=0)
    profit_margin =  models.CharField(max_length=100,default='',null=True, blank=True)
    selling_price_profit_amount = models.FloatField(default=0)
    created_dt =  models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100,default='SYSTEM')
    udpated_Dt = models.DateTimeField(auto_now_add=True)  
    updated_by =  models.CharField(max_length=100,default='SYSTEM')
    #image = models.ImageField(upload_to = 'product_logo', blank = True)
    class Meta:  
        db_table = "product"


class ProductStockDetails(models.Model):  
    stock_id = models.AutoField(primary_key=True,auto_created = True)
    product_id = models.IntegerField()  
    product_sku = models.CharField(max_length=255, null=True, blank=True)
    tot_qty_in_stock = models.FloatField()
    tot_qty_sold = models.FloatField()
    tot_qty_remaining =  models.FloatField()
    tot_qty_returned =  models.FloatField()
    tot_qty_adjusted =  models.FloatField()
    created_dt =  models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100,default='SYSTEM')
    updated_dt = models.DateTimeField(auto_now_add=True)  
    updated_by =  models.CharField(max_length=100,default='SYSTEM')
    class Meta:  
        db_table = "product_stock_dtls"
        
