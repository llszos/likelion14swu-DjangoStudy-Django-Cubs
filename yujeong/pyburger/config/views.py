from django.shortcuts import render     # render 함수를 import
from burgers.models import Burger

def main(request):
    return render(request, "main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    # Template으로 전달해줄 dict 객체
    context = {
        "burgers":burgers,
    }
    return render(request, "burger_list.html", context)