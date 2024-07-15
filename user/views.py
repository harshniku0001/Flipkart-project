from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

# Define a serializer for User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class chek_login(APIView):
    def get(self,request):
        name = request.query_params.get("name")
        get_data = User.objects.get(username=name)
        ser = UserSerializer(get_data)
        return Response(ser.data)




# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'main/login.html')
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or password is not correct")
    return render(request, 'main/login.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'main/signup.html')
    elif request.method == 'POST':
        fname = request.POST.get("first-name")
        lname = request.POST.get("last-name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("confirm-password")
        if password != cpassword:
            return HttpResponse("Your password and confirm password do not match")
        try:
            user = User.objects.create_user(username=fname, email=email, password=password, first_name=fname, last_name=lname)
            user.save()
            return redirect('login')
        except IntegrityError:
            return HttpResponse("Username already exists")
    return render(request, 'main/signup.html')

def logout(request):
    return render(request, 'logout.html')

class Login_API(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            response_data = {
                "message": user.username,
                "password": "hidden"  
            }
            return Response(data=response_data, status=200)
        else:
            return Response(data={"message": "User not found"}, status=404)

    def get(self, request):
        id = request.query_params.get("id")
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(data={"data": serializer.data}, status=200)
        except User.DoesNotExist:
            return Response(data={"message": "User not found"}, status=404)


