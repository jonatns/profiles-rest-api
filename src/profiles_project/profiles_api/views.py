from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):

        an_apiview = [
            'item 1',
            'item2',
            'item3'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
