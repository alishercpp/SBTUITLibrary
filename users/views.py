from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view


@api_view(http_method_names=['GET', "POST"])
def api_login(request):
    if request.method == "POST":
        print(request.data)
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            if user.is_superuser:
                token = Token.objects.get_or_create(user=user)
                if token:
                    return Response({
                        "status": "ok",
                        "user": user.get_username(),
                        "token": token[0].key,
                        "info": "Token get or create successfully"
                    })
                return Response({
                    "status": "failed",
                    "user": user.get_username(),
                    "token": None,
                    "info": "Token not found"
                })
            return Response({
                "status": "failed"
            })
    return Response({
        "status": "nok",
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            if user.is_superuser:
                return HttpResponseRedirect('/admin')
            return redirect('home')
    return render(request, 'login.html')