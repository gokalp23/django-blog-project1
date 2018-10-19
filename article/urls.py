from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard,name="dashboard"),
    path('addarticle/', views.addArticle,name="addarticle"),
    path('article/<int:id>', views.articleDetail,name="articledetail"),
    path('edit/<int:id>', views.editArticle,name="editarticle"),
    path('delete/<int:id>', views.deleteArticle,name="deletearticle"),
    path('deleteconfirm/<int:id>', views.deleteConfirm,name="deleteconfirm"),
    path('', views.showArticles,name="showarticles"),
    path('addcomment/<int:id>', views.addComment,name="addcomment"),
]