from django.shortcuts import render



def blog_view(request):
    context = {"data": "Gfg is the best"}
    return render(request, "blog.html", context)

def post_view(request, post_id):
    context = {"data": "Gfg is the best"}
    return render(request, "post.html", context)