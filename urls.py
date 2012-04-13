from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from forum.models import Board, Thread
from django.contrib.auth.models import User

urlpatterns = patterns('forum.views',
    url(r'^$',
        ListView.as_view(
            queryset=Board.objects.all(),
            template_name='index.html'),
        name='board-list'),
    url(r'^board/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Board,
            template_name='board.html'),
        name='board-detail'),
    url(r'^thread/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Thread,
            template_name='thread.html'),
        name='thread-detail'),
    url(r'^user/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=User,
            template_name='user.html'),
        name='user-detail'),
)
