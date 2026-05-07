from django.shortcuts import render
from blog.models import Post

def post_list(request):
    posts = Post.objects.all() # 모든 Post 객체를 가진 QuerySet
    # 템플릿에 전달할 dict
    context = {
        "posts":posts,
    }
    # 3번째 인수로 템플릿에 데이터 전달
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id) # id값이 URL에서 받은 post_id 값인 Post 객체
    print(post)                         # 가져온 객체를 print 함수로 확인
    context = {
        "post": post,
    }
    return render(request, "post_detail.html", context)