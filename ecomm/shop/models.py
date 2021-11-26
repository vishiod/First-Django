from django.db import models


# Create your models here.
class Product(models.Model):
    # default primary key id given by django is used everywhere
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    publication_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.FloatField(max_length=50, default=0)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contacts'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=5000, default="")
    email = models.CharField(max_length=5000, default="")
    address = models.CharField(max_length=5000, default="")
    city = models.CharField(max_length=5000, default="")
    state = models.CharField(max_length=5000, default="")
    zip_code = models.CharField(max_length=5000, default="")
    phone = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Orders'
