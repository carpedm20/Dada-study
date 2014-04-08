from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import BoardForm, PostForm
from .models import Post
from core.models import StudyGroup

from utils.func import *

########################
# List board
########################

@login_required
def list_board(request):
    form = BoardForm(data=request.POST or None, user=request.user)

    context = RequestContext(request)
    template = 'core/create_board.html'

    if request.method == "POST":
        if form.is_valid():
            board = form.save(commit=False)
            board.save()

            return redirect('/')
        else:
            return create_board_view(request)

    return create_board_view(request)

########################
# View post
########################

@login_required
def view_post(request, study_group_id, post_id):
    context = RequestContext(request)
    template = 'board/view_board.html'

    study_group = StudyGroup.objects.get(unique_id=study_group_id)

    try:
        post = Post.objects.get(id=post_id)
        print post
        return render(request, template, {'study_group': study_group,'post': post, })

    except:
        return redirect('/')

########################
# Create board
########################

@login_required
def create_board(request):
    form = BoardForm(data=request.POST or None, user=request.user)

    context = RequestContext(request)
    template = 'core/create_board.html'

    if request.method == "POST":
        if form.is_valid():
            board = form.save(commit=False)
            board.save()

            return redirect('/')
        else:
            return create_board_view(request)

    return create_board_view(request)

@login_required
def create_board_view(request):
    form = BoardForm(data=request.POST or None, user=request.user)
    template = 'board/create_board.html'

    return render(request, template, {'form': form,  })


########################
# Create post
########################

@login_required
def create_post(request):
    form = PostForm(data=request.POST or None, user=request.user)

    context = RequestContext(request)
    template = 'core/create_post.html'

    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('/')
        else:
            return create_post_view(request)

    return create_post_view(request)

@login_required
def create_post_view(request):
    form = PostForm(data=request.POST or None, user=request.user)
    template = 'board/create_post.html'

    return render(request, template, {'form': form,  })


