from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(verbose_name='标题',max_length=100)
    vum = models.IntegerField(verbose_name='浏览量')
    conten = models.TextField(verbose_name='内容')

