from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Article, Comment
from animations.models import Animation

# Create your views here.
@csrf_exempt
def article(request, animation_pk):
    if request.method =='POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        animation = Animation.objects.get(pk=animation_pk)
        article = Article(title=title, content=content, user=request.user, animation=animation)
        article.save()
        return JsonResponse({"status":"글 등록 완료"})


@csrf_exempt
def comment(request, article_pk, animation_pk):
    if request.method =='POST':
        content = request.POST.get('content', None)
        article = Article.objects.get(pk=article_pk)
        comment = Comment(user=request.user, content=content,article=article)
        comment.save()
        return JsonResponse({"status":"댓글 등록 완료"})
    
    elif request.method =='GET':
        article = Article.objects.get(pk=article_pk)
        comments = list(article.comment_set.all().values())

        return JsonResponse({"comments":comments})




@csrf_exempt
def like(request, article_pk, animation_pk):
    if request.method =='POST':
        article = Article.objects.get(pk=article_pk)
        article.like_users.add(request.user)
        article.save()
        return JsonResponse({"status":"좋아요 완료"})

    elif request.method =="GET":
        article = Article.objects.get(pk=article_pk)
        likes = list(article.like_users.all().values('username'))
        return JsonResponse({"likes":likes})
