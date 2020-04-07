from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Login
from .serializers import LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json
from datetime import datetime
# Create your views here.
class LoginAPIView(APIView):

    def get(self, request):
 #       logindata = Login.objects.all()
        logindata = Login.objects.raw('Select id,login_id,password from login_details')
        serializer = LoginSerializer(logindata,many=True)
        return Response(serializer.data)
       

    def post(self, request):
        username = request.data["login_id"]
        password = request.data["password"]
        count = Login.objects.filter(login_id=username, password = password).count()
        data = ""
        if str(count) == '1':
            data = '{ "data" : "Logged in Successfully", "status" : "success"}'
        else:
            data = '{ "data" : "Invalid Credentials","status" : "failure"}'
        return Response(json.loads(data)) 

class SignUpView(APIView):
    def post(self, request):
        username = request.data["login_id"]
        count = Login.objects.filter(login_id=username).count()
        data = ""
        if str(count) == '0':
            requestValue = request.data
            requestValue['created_date'] = datetime.today().strftime('%Y-%m-%d')
            serializer = LoginSerializer(data=requestValue)
            if serializer.is_valid():
                serializer.save()
                data = '{ "data" : "Account Created Successfully.","status" : "success"}'
                return Response(json.loads(data)) 
        else:
            data = '{ "data" : "Login Id already exists","status" : "failure"}'
            return Response(json.loads(data)) 
        