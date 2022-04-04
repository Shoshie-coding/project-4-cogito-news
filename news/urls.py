from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.home, name="home"),
    path("create", views.PostCreateView.as_view(), name="create"),
    path("stiri/<str:category>", views.stiri, name="stiri"),
    path("myposts", views.MyPostList.as_view(), name="myposts"),
    path('update/<slug:pk>/', views.PostUpdateView.as_view(), name='Post_update'),
    path("thanks", views.thanks, name="thanks"),
    path("multumescfrate", views.multam, name="multu")
]



