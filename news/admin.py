from django.contrib import admin
from .models import Post 
from django_summernote.admin import SummernoteModelAdmin 


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    User summernote for blogpost content
    """
    summernote_fields = ('content')





