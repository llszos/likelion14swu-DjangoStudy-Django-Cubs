from django.db import models

# 게시글
class Post(models.Model):
    # 게시글은 누가 썼는지 User랑 연결됨 (작성자)
    # User 1명이 Post 여러 개 작성 가능
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)
    tags = models.ManyToManyField("posts.HashTag", verbose_name='해시태그 목록', blank=True)

    def __str__(self):
        return f"{self.user.username}의 Post(id: {self.id})"

# 게시글 사진
class PostImage(models.Model):
    # 사진은 어떤 게시글에 속하는지 Post랑 연결됨
    # Post 1개에 PostImage 여러 장 가능
    post = models.ForeignKey(
        Post,
        verbose_name="포스트",
        on_delete=models.CASCADE,
    )
    photo = models.ImageField("사진", upload_to="post")


# 댓글
class Comment(models.Model):
    # 댓글도 누가 썼는지 User랑 연결
    # User 1명이 Comment 여러 개 작성 가능
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )
    # Post 1개에 Comment 여러 개 가능
    post = models.ForeignKey(
        Post,
        verbose_name="포스트",
        on_delete=models.CASCADE,
    )
    content = models.TextField("내용")
    created = models.DateTimeField("생성일시", auto_now_add=True)

class HashTag(models.Model):
    name = models.CharField("태그명", max_length=50)

    def __str__(self):
        return self.name