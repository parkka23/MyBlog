from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from blogska import settings
from .models import PostModel, Category
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _


# Create your views here.


@login_required
def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'blog/index.html', context)


@login_required
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()

            send_comment_notification_email(post.author, post, instance)

            return redirect('blog-post-detail', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'c_form': c_form,
    }
    return render(request, 'blog/post_detail.html', context)

def send_comment_notification_email(user, post, comment):
    # subject = f'Notification: {user.username} commented your post'
    #
    # html_message = render_to_string('email/comment_notification.html', {
    #     'user': user,
    #     'post': post,
    #     'comment': comment,
    # })
    # plain_message = strip_tags(html_message)  # Strip HTML tags for plain text version
    # from_email = settings.EMAIL_HOST_USER  # Use EMAIL_HOST_USER as the from_email
    # to_email = user.email
    #
    # send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

    subject = f'Notification: {user.username} commented your post'
    message = f"Hi {post.author.username},\n\n{user.username} commented on your post:\n\n'{comment}'\n\n"
    from_email = settings.EMAIL_HOST_USER  # Use EMAIL_HOST_USER as the from_email
    to_email = post.author.email

    send_mail(subject, message, from_email, [to_email])
@login_required
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)


@login_required
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post': post
    }
    return render(request, 'blog/post_delete.html', context)


from django.db.models import Q

#
# @login_required
# def index(request):
#     posts = PostModel.objects.all()
#
#     # Handle search
#     query = request.GET.get('q')
#     if query:
#         posts = posts.filter(Q(title__icontains=query))
#
#     if request.method == 'POST':
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.author = request.user
#             instance.save()
#             return redirect('blog-index')
#     else:
#         form = PostModelForm()
#
#     context = {
#         'posts': posts,
#         'form': form,
#         'query': query,  # Pass the query for display in the template
#     }
#
#     return render(request, 'blog/index.html', context)

@login_required
def index(request):
    categories = Category.objects.all()
    posts = PostModel.objects.all()
    category_filter = request.GET.get('category')  # Get the selected category from the request

    if category_filter:
        posts = posts.filter(category=category_filter)  # Filter posts by the selected category

    # Handle search
    query = request.GET.get('q')
    if query:
        posts = posts.filter(Q(title__icontains=query))

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()

    context = {
        'posts': posts,
        'form': form,
        'query': query,
        'categories': categories,
        'category_filter': category_filter,
        # Pass the query for display in the template
    }

    return render(request, 'blog/index.html', context)
