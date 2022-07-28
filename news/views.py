import requests
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from .models import Post
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CommentForm


def post_likes(request, pk):
    """Renders post likes"""
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('Post_detail', args=[post.slug]))


class PostDetailView(generic.detail.DetailView):
    """Renders post detail view"""
    model = Post
    template_name = "post_detail.html"


def get_context_data(self, **kwargs):
    """Renders likes view"""
    data = super().get_context_data(**kwargs)

    likes_connected = get_object_or_404(Post, slug=self.kwargs['slug'])
    liked = False
    if likes_connected.likes.filter(id=self.request.user.id).exists():
        liked = True
    data['number_of_likes'] = likes_connected.number_of_likes()
    data['post_is_liked'] = liked
    return data


class PostUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Renders the update view"""
    model = Post
    fields = [
        'title',
        'slug',
        'featured_image',
        'category',
        'content',
        'excerpt']
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 0
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('thanks')
        messages.success(
            request, 'Post was successfully added'
        )


class PostCreateView(LoginRequiredMixin, generic.edit.CreateView):
    """Renders the post creation view"""

    model = Post
    fields = [
        "title",
        "slug",
        "featured_image",
        "category",
        "content",
        "excerpt"]
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def get_success_url(self):
        """Returns thank you page after posting"""
        return reverse('thanks')


def thankyou(request):
    """Returns thank you page after signup"""
    return render(request, "thankyou.html")


def home(request):
    """Returns homepage"""
    return render(request, "index.html")


def thanks(request):
    """Returns thanks page after posting"""
    return render(request, "thanks.html")


def delete_post(request, pk):
    """Returns delete page"""
    if request.method == "POST":
        Post.objects.get(pk=int(pk)).delete()
        return HttpResponseRedirect(reverse('myposts'))


def blogs(request, category):
    """Renders blogs news categories"""
    user_posts = Post.objects.filter(category=category)
    url = ('https://newsapi.org/v2/everything?'
           'q={}&'
           'from=2022-06-28&'
           'sortBy=popularity&'
           'pageSize=5&'
           'apiKey=b336f8d783094ae1b6a923721064ccdd'.format(category))
    print(url)
    response = requests.get(url)
    print(response.json())
    return render(
        request, "blogs.html", {
            'data': response.json()['articles'], 'user_posts': user_posts})


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter().order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5


class MyPostList(generic.ListView):
    """Returns my posts page"""
    model = Post
    template_name = 'myposts.html'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class ArticleDetailView(View):
    """
    View for an individual article page
    """
    model = Post()
    template_name = 'article_details.html'
