from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from .models import Post
class Homepageview(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ID"] = Post.objects.all()  
        return context


class PostDetailview(DetailView):
    template_name = 'detail.html'
    model = Post

    


# Create your views here.
