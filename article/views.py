from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm,CommentForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Makaleniz başarı ile kaydedilmiştir.")
        return redirect("article:dashboard")


    return render(request,"addarticle.html",context)


def articleDetail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id=id)

    comments = article.comments.all()

    return render(request,"articledetail.html",{"article":article,"comments":comments})

@login_required(login_url="user:login")
def editArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Makaleniz başarı ile güncellenmiştir.")
        return redirect("article:dashboard")

    return render(request,"editarticle.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale başarı ile silinmiştir.")

    return redirect("article:dashboard")

@login_required(login_url="user:login")
def deleteConfirm(request,id):
    article = get_object_or_404(Article,id=id)
    return render(request,"deleteconfirm.html",{"article":article})  


def showArticles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"showarticles.html",{"articles":articles})
    
    article_list = Article.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(article_list, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request,"showarticles.html",{"articles":articles})    


def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        newComment = form.save(commit=False)
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
        
    return redirect(reverse("article:articledetail",kwargs={"id":id}))


