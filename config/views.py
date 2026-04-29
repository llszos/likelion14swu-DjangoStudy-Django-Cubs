from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def post_detail(request):
    return render(request, 'post_detail.html')