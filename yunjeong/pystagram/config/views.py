from django.shortcuts import render, redirect

def index(request):
    # 로그인되어 있는 경우, 피드 페이지로 redirect
    if request.user.is_authenticated:
        return redirect("posts:feeds")
    else:
        return redirect("users:login")