from django.db import models

class CustomerInformations(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=100, blank=True, null=True)
    email_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_informations'

class Orders(models.Model):
    product = models.ForeignKey('Products', models.DO_NOTHING)
    customer = models.ForeignKey(CustomerInformations, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders'





