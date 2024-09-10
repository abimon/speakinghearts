from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import User

class  Article(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to=settings.MEDIA_ROOT+'upload/cover')
    content = models.TextField()
    pub_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)
    def __str__(self):
        return self.title
    
class Poem(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to=settings.MEDIA_ROOT+'upload/cover')
    content = models.TextField()
    pub_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)
    def __str__(self):
        return self.title

class Music(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    cover = models.FileField(upload_to=settings.MEDIA_ROOT+'upload/music')
    content = models.TextField()
    composer = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(default=now)
    def __str__(self):
        return self.title
class ArticleViewers(models.Model):
    ip=models.CharField(max_length=20)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
class ArticleLikes(models.Model):
    ip=models.CharField(max_length=20)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
class ArticleComments(models.Model):
    ip=models.CharField(max_length=20)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
class PoemComments(models.Model):
    ip=models.CharField(max_length=20)
    article = models.ForeignKey(Poem,on_delete=models.CASCADE)
class PoemViewers(models.Model):
    ip=models.CharField(max_length=20)
    article = models.ForeignKey(Poem,on_delete=models.CASCADE)
class PoemLikes(models.Model):
    ip=models.CharField(max_length=20)
    article = models.ForeignKey(Poem,on_delete=models.CASCADE)
class MusicComments(models.Model):
    ip=models.CharField(max_length=20)
    article = models.ForeignKey(Music,on_delete=models.CASCADE)
class MusicViewers(models.Model):
    ip=models.CharField(max_length=20)
    article = models.ForeignKey(Music,on_delete=models.CASCADE)
class MusicLikes(models.Model):
    ip=models.CharField(max_length=20)
    article = models.ForeignKey(Music,on_delete=models.CASCADE)