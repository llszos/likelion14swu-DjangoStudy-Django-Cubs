from posts.forms import CommentForm, PostForm
from django.shortcuts import render, redirect
from posts.models import Post, Comment, PostImage, HashTag
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

def feeds(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }

    return render(request, "posts/feeds.html", context)

@require_POST
def comment_add(request):

    form = CommentForm(data=request.POST)

    if form.is_valid():

        comment = form.save(commit=False)
        comment.user = request.user

        comment.save()

        print(comment.id)
        print(comment.content)
        print(comment.user)

        url = reverse("posts:feeds") + f"#post-{comment.post.id}"
        return HttpResponseRedirect(url)

def comment_delete(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        if comment.user == request.user:
            comment.delete()
            url = reverse("posts:feeds") + f"#post-{comment.post.id}"
            return HttpResponseRedirect(url)
        else:
            return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")


def post_add(request):
    if request.method == "POST":
        # request.POST로 온 데이터 ("content")는 PostForm으로 처리
        form = PostForm(request.POST)

        if form.is_valid():
            # Post의 "user" 값은 request에서 가져와 자동 할당한다.
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            # Post를 생성한 후
            # request.FILES.getlist("images")로 전송된 이미지들을 순회하며 PostImage 객체를 생성한다
            for image_file in request.FILES.getlist("images"):
                # request.FILES 또는 reqeust.FILES.getlist()로 가져온 파일은
                # Model의 ImageField 부분에 곧바로 할당한다
                PostImage.objects.create(
                    post=post,
                    photo=image_file,
                )

            tag_string = request.POST.get("tags")
            if tag_string:
                tag_names = [tag_name.strip() for tag_name in tag_string.split(",")]
                for tag_name in tag_names:
                    tag, _ = HashTag.objects.get_or_create(name=tag_name)
                    # get_or_create로 생성하거나 가져온 HashTag 객체를 Post의 tags에 추가한다
                    post.tags.add(tag)

            # 모든 PostImage와 Post의 생성이 완료되면
            # 피드 페이지로 이동하여 생성된 Post의 위치로 스크롤되도록 한다
            url = reverse("posts:feeds") + f"#post-{post.id}"
            return HttpResponseRedirect(url)

    else:
        form = PostForm()

    context = {"form": form}
    return render(request, "posts/post_add.html", context)



def tags(request, tag_name):
    try:
        tag = HashTag.objects.get(name=tag_name)
    except HashTag.DoesNotExist:
        # tag_name에 해당하는 HashTag를 찾지 못한 경우, 빈 QuerySet을 돌려준다.
        posts = Post.objects.none()
    else:
        posts = Post.objects.filter(tags=tag)

    context = {
        "tag_name": tag_name,
        "posts": posts,
    }
    return render(request, 'posts/tags.html', context)