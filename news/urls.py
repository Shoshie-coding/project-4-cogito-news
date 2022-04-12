from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.home, name="home"),
    path("create", views.PostCreateView.as_view(), name="create"),
    path("blogs/<str:category>", views.blogs, name="blogs"),
    path("myposts", views.MyPostList.as_view(), name="myposts"),
    path('update/<slug:pk>/', views.PostUpdateView.as_view(), name='Post_update'),
    path('delete_post/<int:pk>', views.delete_post, name="delete_post"),
    path('post-like/<int:pk>', views.PostLike, name="post_like"),
    path("thanks", views.thanks, name="thanks"),
    path("confirm", views.thankyou, name="thankstoyou"),
    path('<slug:slug>', views.PostDetailView.as_view(), name='Post_detail'),
]