from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status

from blog.models.post import BlogPost
from uauth.model.user import User

def post_view(request, post_id):
    context = {"data": "Gfg is the best"}
    post = BlogPost.objects(id=post_id).first()
    context["post"] = post
    return render(request, "post.html", context)


class BlogPostRetrieveUpdateDeleteAPI(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        return BlogPost.objects(id=pk).first()

    def get(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'detail': 'Not found'}, status=404)
        return {
            "id": str(obj.id),
            "title": obj.title,
            "content": obj.content,
            "published_at": obj.published_at,
            "is_published": obj.is_published
       }

    def put(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'detail': 'Not found'}, status=404)
        title = request.data.get("title")
        content = request.data.get("content")
        is_published = request.data.get("is_published")
        if title is not None:
            obj.title = title
        if content is not None:
            obj.content = content
        if is_published is not None:
            obj.is_published = is_published
        obj.save()
        return self.get(request, pk)


    def delete(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response({'detail': 'Not found'}, status=404)

        obj.delete()
        return Response(status=204)