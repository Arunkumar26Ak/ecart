from django.db import models

class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    customer_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'