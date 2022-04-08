from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from .models import Post
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
import requests
#b336f8d783094ae1b6a923721064ccdd

def PostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('Post_detail', args=[post.slug]))



class PostDetailView(generic.detail.DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, slug=self.kwargs['slug'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data



class PostUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Post
    fields = ['title', 'slug', 'featured_image', 'category', 'content', 'excerpt'] 
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 0
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('thanks')


class PostCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Post
    fields = ['title', 'slug', 'featured_image', 'category', 'content', 'excerpt'] 
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 0
        return super().form_valid(form)

        return render(
                request,
                "post_detail.html",
                {
                    "post": post,
                    "comments": comments,
                    "commented": False,
                    "liked": liked,
                    "comment_form": CommentForm()
                },
            )

    def get_success_url(self):
        return reverse('thanks')

def thankyou(request):
    return render(request, "thankyou.html")

def home(request):
    return render(request, "index.html")

def thanks(request):
    return render(request, "thanks.html")

def blogs(request, category):
    user_posts = Post.objects.filter(category=category, status = 1)

    url = ('https://newsapi.org/v2/everything?'
       'q={}&'
       'from=2022-03-28&'
       'sortBy=popularity&'
       'pageSize=5&'
       'apiKey=b336f8d783094ae1b6a923721064ccdd'.format(category))
    print(url)
    response = requests.get(url)
    print(response.json()['articles'])
    return render(request, "blogs.html", {'data': response.json()['articles'], 'user_posts': user_posts})

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5



class MyPostList(generic.ListView):
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
    
