from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status

from blog.models.post import BlogPost
from uauth.model.user import User

def generate_blog_context():
    #cache this view context
    user = User.objects(email="ibhatia1998@gmail.com").first()
    posts = BlogPost.objects(is_published=True, created_by = user).order_by('-published_at')
    print(posts)
    return {
        'posts':posts
    }

def blog_view(request):
    context = {"data": "Gfg is the best"}
    return render(request, "blog.html", generate_blog_context())



class BlogPostListCreateAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        posts = BlogPost.objects.all().order_by('-created_at')
        post_data = [{
            "id": str(post.id),
            "title": post.title,
            "content": post.content,
            "published_at": post.published_at,
            "is_published": post.is_published
        } for post in posts]
    
    

