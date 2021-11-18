from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Board, Post
from .forms import NewTopicForm
from django.contrib import messages

def home(req):
    boards = Board.objects.all()
    return render(req, 'home.html', {'boards': boards})


def topics(req, board_id) :
    board = get_object_or_404(Board, pk=board_id)
    return render(req, 'topics.html', {'board':board})

def new_topic(req, board_id) :
    board = get_object_or_404(Board, pk=board_id)
    user = User.objects.get(is_active = True)
    form = NewTopicForm(req.POST or None)
    if req.method == 'POST' :
        if form.is_valid() : 
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = user
            )
            return redirect('board_topics', board_id=board.pk)

    return render(req, 'new_topic.html', {'board': board, 'form': form})

