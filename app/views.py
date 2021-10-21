from django.shortcuts import render

from django.http import HttpResponseRedirect

from .models import Post, Comment, SavePost


def post_list(request):
	posts = Post.objects.all()

	return render(request, 'post_list.html', {'posts': posts})


def save_post(request, slug):
	post = Post.objects.get(slug=slug)
	save = SavePost.objects.all()
	if request.method == 'GET':
		obj, save = SavePost.objects.get_or_create(post=post)

		return HttpResponseRedirect('/')

	return render(request, 'saved_posts.html', {'post': post, 'save': save})


def saved_posts(request):
	save = SavePost.objects.all()

	return render(request, 'saved.html', {'save': save})


def add_comment(request, slug):
	pass