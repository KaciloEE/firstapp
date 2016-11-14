from django.conf.urls import url, include
from article.views import articles, article, addlike, addcomment


urlpatterns = [
  #url(r'^1/', basic_one, name='basic_one'),
  #url(r'^2/', template_two, name='template_two'),
  #url(r'^3/', template_three_simple, name='template_three_simple'),
  #url(r'^articles/all/$', articles, name='articles'),
  url(r'^articles/get/(?P<article_id>\d+)/$', article, name='article'),
  url(r'^articles/addlike/(?P<article_id>\d+)/$', addlike, name='addlike'),
  url(r'^articles/addcomment/(?P<article_id>\d+)/$', addcomment, name='addcomment'),
  url(r'^page/(\d+)/$', articles, name='articles'),
  url(r'^$', articles, name='articles')
]
