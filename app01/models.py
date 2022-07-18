from django.db import models

# Create your models here.
from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name='小组名称',max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(verbose_name='学生名字',max_length=10)
    age = models.IntegerField(verbose_name='年龄')
    group = models.ForeignKey(to=Group,on_delete=models.CASCADE)



