from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from forum.models import Board, Thread
from django.contrib.auth.models import User

urlpatterns = patterns('forum.views',
    url(r'^$',
        ListView.as_view(queryset=Board.objects.all()),
        name='forum-board-list'),
    url(r'^board/(?P<pk>\d+)/$',
        DetailView.as_view(model=Board),
        name='forum-board-detail'),
    url(r'^thread/(?P<pk>\d+)/$',
        DetailView.as_view(model=Thread),
        name='forum-thread-detail'),
    url(r'^user/(?P<pk>\d+)/$',
        DetailView.as_view(model=User),
        name='forum-user-detail'),
)
