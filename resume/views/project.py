from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from resume.model.project import Project


class ProjectCRUDAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        projects = Project.objects.all().order_by('-published_date')
        project_data = [{
            "id": str(project.id),
            "name": project.name,
            "published_date": project.published_date,
           "description": [
                item.to_dict() for item in project.description
            ],
            "link": project.link
        } for project in projects]
        return Response(project_data)

    def post(self, request):
        name = request.data.get("name")
        published_date = request.data.get("published_date")
        description = request.data.get("description", [])
        link = request.data.get("link", "")

        if not name:
            return Response({"error": "Name is required."}, status=status.HTTP_400_BAD_REQUEST)

        project = Project(
            name=name,
            published_date=published_date,
            description=description,
            link=link
        )
        project.save()
        return Response({
            "id": str(project.id),
            "name": project.name,
            "published_date": project.published_date,
           "description": [
                item.to_dict() for item in project.description
            ],
            "link": project.link
        }, status=status.HTTP_201_CREATED)

    def put(self, request, project_id):
        project = Project.objects(id=project_id).first()
        if not project:
            return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)

        name = request.data.get("name")
        published_date = request.data.get("published_date")
        description = request.data.get("description")
        link = request.data.get("link")

        if name:
            project.name = name
        if published_date:
            project.published_date = published_date
        if description is not None:
            project.description = description
        if link is not None:
            project.link = link

        project.save()
        return Response({
            "id": str(project.id),
            "name": project.name,
            "published_date": project.published_date,
           "description": [
                item.to_dict() for item in project.description
            ],
            "link": project.link
        }, status=status.HTTP_200_OK)

    def delete(self, request, project_id):
        project = Project.objects(id=project_id).first()
        if not project:
            return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)

        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    