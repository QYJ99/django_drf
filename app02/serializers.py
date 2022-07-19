# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 19:18
# @Author  : Cat
# @FileName: serializers.py


from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100,required=True)
    vnum = serializers.IntegerField(required=True)
    content = serializers.CharField()

    def create(self,validated_data):
        return Article.objects.create(**validated_data)


    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.vnum = validated_data.get('vnum', instance.vnum)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


