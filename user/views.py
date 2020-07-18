from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User


# Create your views here.


def login_view(request):
    error = ""
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            error = "아이디나 비밀번호가 일치하지 않습니다."
    return render(request, "user/login.html", {"error": error})


def logout_view(request):
    logout(request)
    return redirect("user:login")


def signup_view(request):
    error = ""
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]
        major = request.POST["major"]

        try:
            user = User.objects.create_user(username, email, password)
        except Exception:
            error = "이미 존재하는 아이디 입니다."
            return render(request, "user/signup.html", {"error": error})

        user.firstname = firstname
        user.lastname = lastname
        user.student_id = student_id
        user.major = major
        user.save()
        login(request, user)

        return redirect("user:login")

    return render(request, "user/signup.html", {"error": error})
