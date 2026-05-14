from django.contrib import contenttypes
from django.shortcuts import render, redirect
from blog.models import Post, Comment

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
    if request.method == "POST":
        comment_content = request.POST["comment"] # textare의 "name" 속성값 ("comment")을 가져온다
        Comment.objects.create( #전달된 "comment"의 값으로 Comment 객체를 생성한다.
            post=post,
            content=comment_content,
        )

    #GET 요청이나 POST 요청 모두 이 글의 상세 페이지 보여주기
    context = {
        "post": post,
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST": #method가 POST일 때
        print("method POST")
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"] #이미지 파일
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,
        )
        return redirect(f"/posts/{post.id}/") #작성한 글의 상세페이지로 이동

    #POST/GET 중 어느 요청이든 render 결과를 리턴
    return render(request, "post_add.html")