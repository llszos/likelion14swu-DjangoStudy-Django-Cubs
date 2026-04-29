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
