from django.db import models

from django.contrib.auth.models import User


class Comment(models.Model):
    "Довление комминтариев для постов"
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.user.name


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class SavePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title