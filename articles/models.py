from django.db import models
#settings에 AUTH_USER_MODEL등록했으므로 사용가능
from django.conf import settings
from animations.models import Animation

# Create your models here.
class Article(models.Model): # 상속
    # id는 자동으로 만들어진다.
    title = models.CharField(max_length=50)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    animation = models.ForeignKey(Animation, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)

    def __str__(self):
        return f'{self.title}'



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return f'{self.user} {self.content}'



