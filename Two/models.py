from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=200)
    s_age = models.IntegerField(default=1)

class Person(models.Model):
    p_name = models.CharField(max_length=20, db_column='name')
    p_age = models.IntegerField(default=20, db_column='age')
    p_sex = models.BooleanField(default=True, db_column='sex')
    class Meta:
        db_table = 'People'
#重写隐形属性，is_delete=Ture为删除
class MyManager(models.Manager):
    def get_queryset(self):
        return super(MyManager, self).get_queryset().filter(is_delete=False)

class Animal(models.Model):
    a_name = models.CharField(max_length=10)
    is_delete = models.BooleanField(default=False)
    #自已定义显性属性
    objects = MyManager()
