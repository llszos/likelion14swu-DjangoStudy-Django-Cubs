import admin_thumbnails
from django.contrib import admin
from posts.models import Post, PostImage, Comment, HashTag
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
    ]
    inlines = [
        CommentInline,
        PostImageInline,
    ]
    # Post 변경 화면에서 ManyToManyField를 Checkbox로 출력
    formfield_overrides = {
        ManyToManyField: {"widget": CheckboxSelectMultiple},
    }

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
    ]

@admin.register(HashTag)
class HashtagsAdmin(admin.ModelAdmin):
    pass