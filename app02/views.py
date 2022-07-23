from django.shortcuts import render
from .models import *
from .serializers import ArticleSerializer #TagSerializer, CategorySerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        arts = Article.objects.all()
        ser = ArticleSerializer(instance=arts, many=True, context={'request': request})
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data, content_type='application/json', status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)  # 把前端传过来的json数据转成python里面数据类型

        ser = ArticleSerializer(data=data, context={'request': request})

        if ser.is_valid():
            ser.save()
            json_data = JSONRenderer().render(ser.data)
            return HttpResponse(json_data, content_type='application/json', status=201)
        json_data = JSONRenderer().render(ser.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)


@csrf_exempt
def article_detail(request, pk):
    try:
        art = Article.objects.get(pk=pk)
    except Article.DoesNotExist as e:
        # return HttpResponse(status=404)
        pass

    if request.method == 'GET':
        ser = ArticleSerializer(instance=art, context={'request': request})
        return JSONResponse(ser.data, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        ser = ArticleSerializer(instance=art, data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data, status=201)
        return JSONResponse(ser.errors, status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        ser = ArticleSerializer(instance=art, data=data, partial=True, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data, status=201)
        return JSONResponse(ser.errors, status=400)

    elif request.method == 'DELETE':
        art.delete()
        return HttpResponse(status=204)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        ser = ArticleSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JSONResponse(ser.data, status=201)
        return JSONResponse(ser.errors, status=400)