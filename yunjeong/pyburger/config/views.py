from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

# #main 함수 정의
# def main(request):
#     return HttpResponse("안녕하세요, pyburger입니다.")
#
# #버거의 종류를 알려주는 직원 역할
# def burger_list(request):
#     return HttpResponse("pyburger의 햄버거 목록입니다.")

def main(request):
	return render(request, "main.html")

def burger_list(request):
	burgers = Burger.objects.all()
	print("전체 햄버거 목록:", burgers)

	#Template으로 전달해줄 dict 객체
	context = {
		"burgers": burgers, #burgers 키에 burgers 변수(QuerySet 객체)를 전달한다.
	}
	#render 함수의 마지막에 context 전달
	return render(request, "burger_list.html", context)

# 버거 검색
def burger_search(request):
    # print(request.GET) #request.GET으로 전달된 데이터를 출력
    # request.GET에서 "keyword" 키의 값을 가져와 출력
    keyword = request.GET.get("keyword")
    # print(keyword)
    # 이름(name 속성)에 전달받은 키워드 값이 포함된 Burger를 검색한다.
    # burgers = Burger.objects.filter(name__contains=keyword)
    # print(burgers)

    #keyword 값이 주어진 경우
    if keyword is not None:
        # keyword 값으로 검색된 QuerySet을 할당
        burgers = Burger.objects.filter(name__contains=keyword)

    # 주소표시줄을 통해 keyword가 주어지지 안항, None이 할당된 경우
    else:
        # 검색 결과가 없는 것과 같은 빈 QuerySet을 할당
        burgers = Burger.objects.none()
        
    context = {
        "burgers":burgers,
    }

    return render(request, "burger_search.html", context)