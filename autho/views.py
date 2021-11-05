from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response


class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = self.request.query_params
        return Response(data)
