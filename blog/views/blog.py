from django.shortcuts import render
from blog.model.post import BlogPost
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

def post_view(request, post_id):
    context = {"data": "Gfg is the best"}
    post = BlogPost.objects(id=post_id).first()
    context["post"] = post
    return render(request, "post.html", context)