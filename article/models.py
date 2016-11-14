from django.db import models
from django.contrib.auth.forms import User

# Create your models here.
class Article(models.Model):
  class Meta:
    db_table = "article"

  article_title = models.CharField(max_length=200)
  article_text = models.TextField()
  article_date = models.DateTimeField()
  article_likes = models.IntegerField(default=0)

class Comments(models.Model):
  class Meta:
    db_table = "comments"

  comments_date = models.DateTimeField(blank=True, null=True)
  comments_text = models.TextField(verbose_name="Добавить комментарии")
  comments_article = models.ForeignKey(Article)
  comments_from = models.ForeignKey(User,blank=True, null=True)

