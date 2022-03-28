from django.shortcuts import render
from django.views import generic, View
from .models import Post
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
#b336f8d783094ae1b6a923721064ccdd


class PostCreateView(generic.edit.CreateView):
    model = Post
    fields = '__all__' 
    template_name = "post_form.html"

def home(request):
    return render(request, "index.html")



def stiri(request, category):
    user_posts = Post.objects.filter(category=category)

    url = ('https://newsapi.org/v2/everything?'
       'q={}&'
       'from=2022-03-28&'
       'sortBy=popularity&'
       'apiKey=b336f8d783094ae1b6a923721064ccdd'.format(category))
    print(url)
    response = requests.get(url)
    print(response.json()['articles'])
    return render(request, "stiri.html", {'data': response.json()['articles'], 'user_posts': user_posts})

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5

class ArticleDetailView(View):
    """
    View for an individual article page
    """
    model = Post()
    template_name = 'article_details.html'
    
