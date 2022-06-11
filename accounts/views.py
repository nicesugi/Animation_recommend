from django.http import JsonResponse
from django.shortcuts import render
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

# Create your views here.
@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        new_user = User()
        new_user.username = username
        new_user.set_password(password)
        new_user.save()
        return JsonResponse({"status":"success"})


@csrf_exempt
def view_login(request):
    if request.method =='POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password) # 사용자 불러오기
        if user is  not None:
            login(request, user)
            return JsonResponse({"status":"로그인 성공!"})
        else:
            return JsonResponse({"status": "user none"})
    else:
        return JsonResponse({"status":"method"})



@csrf_exempt
def follow(request, username):
    if request.method =='POST':
        target_user = User.objects.get(username=username)
        user = request.user
        user.follow.add(target_user)
        user.save()
        return JsonResponse({"status":"follow 완료"})

@csrf_exempt
def view_follow(request):
    if request.method =='GET':
        user = request.user
        following = list(user.follow.all().values('username'))
        return JsonResponse({"following":following})

@csrf_exempt
def view_like(request):
    if request.method =='GET':
        user = request.user
        likes = list(user.like_articles.all().values())
        return JsonResponse({"likes":likes})