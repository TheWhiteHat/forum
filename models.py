from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=126)
    desc = models.CharField(max_length=126)
    def __unicode__(self):
        return self.name

class Thread(models.Model):
    name = models.CharField(max_length=126)
    board = models.ForeignKey(Board)
    creator = models.ForeignKey(User)
    created = models.DateTimeField();
    views = models.IntegerField()
    def __unicode__(self):
        return '%s (%s)' % (self.name, self.board.name)

class Post(models.Model):
    poster = models.ForeignKey(User)
    thread = models.ForeignKey(Thread)
    time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    def __unicode__(self):
        return '%s (%s): %s...' % (self.poster.username, str(self.time), self.content[:50])
