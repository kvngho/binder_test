from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
import requests

ID = '1013430102836002'
SECRET = '53714de5a51b0af492466e5260c5f401'
class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = self.request.query_params
        code = data.get('code', None)
        data = {'code': code, 'grant_type': 'authorization_code', 'client_id': ID, 'client_secret': SECRET,
                'redirect_uri': 'https://kangho.space/autho/'}
        res = requests.post('https://api.instagram.com/oauth/access_token', data=data)
        return Response(res.json())

# class RedirectAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         data = self.request.DATA
#         code = data.get('code', None)
#         data = {'code': code, 'grant_type': 'authorization_code', 'client_id': ID, 'client_secret': SECRET,
#                 'redirect_uri': 'https://kangho.space/autho/'}
#         res = requests.post('https://api.instagram.com/oauth/access_token', data=data)
#         return Response(res.json())