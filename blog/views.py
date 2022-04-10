from datetime import time
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, "blog/post_list.html", {"posts":posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post":post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) #formの内容取得＆PostForm構築
        if form.is_valid():
            post = form.save(commit=False) #まだしない。
            post.author = request.user #PostForm内にauthor属性がないので必須。
            post.save()
            return redirect('post_detail', pk=post.pk) #新しい投稿のpost_detailをリダイレクト。
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form":form})