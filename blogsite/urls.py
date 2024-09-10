from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="Index"),
    path("articles/",views.articles,name="Index"),
    path("articles/<int:id>",views.article,name="Article"),
    path("poems/",views.poems,name="poems"),
    path("poem/<int:id>",views.poem,name="poem"),
    path("music/",views.music,name="music"),
]
