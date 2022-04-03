from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.home, name="home"),
    path("create", views.PostCreateView.as_view(), name="create"),
    path("stiri/<str:category>", views.stiri, name="stiri"),
    path("thanks", views.thanks, name="thanks")
]



