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
from simplecrypt import encrypt, decrypt
from datetime import datetime
# Create your views here.
class LoginAPIView(APIView):

    def get(self, request):
        logindata = Login.objects.raw('Select id,login_id,password from login_details')
        serializer = LoginSerializer(logindata,many=True)
        return Response(serializer.data)
       

    def post(self, request):
        username = str(request.data["user_name"])
        password = str(request.data["password"])
        count = Login.objects.filter(user_name=username, password = password, active_flag= 1  ).count()
        # logindata = Login.objects.raw("Select user_id,password from user_login where user_name='"+username+"'")
        # serializer = LoginSerializer(logindata,many=True)
        data = ""
        # if(((serializer.data)) == []):
        #     data = '{ "data" : "Invalid Credentials","status" : "failure"}'
        #     return Response(json.loads(data))
        # else: 
        #     jsonData = json.dumps(serializer.data[0])
        #     decryptedPassword = decrypt(password, (json.loads(jsonData)["password"].decode('ASCII')))
        #     print("%%%%%%%%%%%%%%%%"+decryptedPassword)
        #     if str(decryptedPassword) == 'valid password':
        #         data = '{ "data" : "Logged in Successfully", "status" : "success"}'
        #     else:
        #         data = '{ "data" : "Invalid Credentials","status" : "failure"}'
        if str(count) == '1':
            data = '{ "data" : "Logged in Successfully", "status" : "success"}'
        else:
            data = '{ "data" : "Invalid Credentials","status" : "failure"}'
        return Response(json.loads(data)) 

class SignUpView(APIView):
    def post(self, request):
        username = request.data["user_name"]
        count = Login.objects.filter(user_name=username).count()
        data = ""
        if str(count) == '0':
            requestValue = request.data
            # encryptedpassword = (encrypt(requestValue["password"],'valid password'))
            # requestValue["password"] = str(encryptedpassword)
            # print("************************ "+str(encryptedpassword))
            # decryptedPassword = decrypt(requestValue["password"], encryptedpassword)
            # print(decryptedPassword)
            serializer = LoginSerializer(data=requestValue)
            if serializer.is_valid():
                serializer.save()
                data = '{ "data" : "Account Created Successfully.","status" : "success"}'
                return Response(json.loads(data))
            else:
                data = '{ "data" : "Some Error Occured","status" : "failure"}'
                return Response(json.loads(data))
        else:
            data = '{ "data" : "Login Id already exists","status" : "failure"}'
            return Response(json.loads(data)) 
        