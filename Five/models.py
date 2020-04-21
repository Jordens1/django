from django.db import models

# Create your models here.

class Person(models.Model):
    s_name = models.CharField(max_length=16)
    s_sex = models.BooleanField(default=False)

class Idcard(models.Model):
    id_num = models.CharField(max_length=20, unique=True)
    id_person = models.OneToOneField(Person, null=True, blank=True, on_delete=models.PROTECT)


class Customer(models.Model):
    c_name = models.CharField(max_length=20)

class Good(models.Model):
    g_name = models.CharField(max_length=20)
    g_customer = models.ManyToManyField(Customer)




















