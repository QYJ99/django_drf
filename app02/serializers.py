# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 19:18
# @Author  : Cat
# @FileName: serializers.py

from rest_framework import serializers
from .models import Article,Category



# 普通序列化
# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100,required=True)
#     vnum = serializers.IntegerField(required=True)
#     content = serializers.CharField()
#
#     def create(self,validated_data):
#         return Article.objects.create(**validated_data)
#
#
#     def update(self,instance,validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.vnum = validated_data.get('vnum', instance.vnum)
#         instance.content = validated_data.get('content', instance.content)
#         instance.save()
#         return instance


# 模型序列化
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         # fields = ('id', 'vum', 'content', 'title')
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# StringRelatedField
# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#     class Meta:
#         model = Article
#         # fields = ('id', 'vum', 'content', 'title')
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.StringRelatedField(many=True)
#     class Meta:
#         model = Category
#         # fields = '__all__'
#         fields = ('id','name','articles')

# PrimaryKeyRelatedField
# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.PrimaryKeyRelatedField(read_only=True)
#     class Meta:
#         model = Article
#         # fields = ('id', 'vum', 'content', 'title')
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
#     class Meta:
#         model = Category
#         # fields = '__all__'
#         fields = ('id','name','articles')


# HyperlinkedRelatedField
# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.HyperlinkedRelatedField(
#         view_name='app02:category-detail',
#         read_only=True,
#         # lookup_field='id'
#     )
#     class Meta:
#         model = Article
#         # fields = ('id', 'vum', 'content', 'title')
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = serializers.HyperlinkedRelatedField(
#         view_name='app02:article-detail',
#         read_only=True,
#         # lookup_field='id'
#         many=True,
#     )
#     class Meta:
#         model = Category
#         # fields = '__all__'
#         fields = ('id','name','articles')

# SlugRelatedField
class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name' # 返回的值
    )
    class Meta:
        model = Article
        # fields = ('id', 'vum', 'content', 'title')
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    articles = serializers.SlugRelatedField(
        read_only=True,
        slug_field='content',  # 返回的值
        many=True,
    )
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ('id','name','articles')



