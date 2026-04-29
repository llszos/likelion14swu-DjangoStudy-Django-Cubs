from django.http import HttpResponse

def main(request):
    return HttpResponse("안녕하세요, pyburger입니다.")

def burger_list(request):
    return HttpResponse("pyburger의 햄버거 목록입니다.")

from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def burger_list(request):
    return render(request, "burger_list.html")

from burgers.models import Burger

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록: ", burgers)

    context = {
        "burgers": burgers,
    }
    return render(request, "burger_list.html", context)