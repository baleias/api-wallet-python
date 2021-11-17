from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return HttpResponse('<h1>Hello, World<h1>')

@api_view(['GET', 'POST'])
def hello_world(request):
    obj = {'message': "got some data!", 'data': request.data}
    if request.method == 'POST':
        return Response({'message': obj['message'], 'data': obj['data']})
    return Response({'message': 'Hello again, World\'s!'})