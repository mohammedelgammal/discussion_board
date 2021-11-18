from django.db import models
from django.contrib.auth.models import User

class Board(models.Model) :
    name = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Topic(models.Model) :
    subject = models.CharField(max_length=30)
    board = models.ForeignKey(
        Board,
        related_name='topics',
        on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        User,
        related_name='topics',
        on_delete=models.CASCADE
    )
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Post(models.Model) :
    message = models.TextField(max_length=5000)
    topic = models.ForeignKey(
        Topic, 
        related_name='posts',
        on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message