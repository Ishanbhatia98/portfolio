from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from resume.model.skill import Skill


class SkillCRUDAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        skills = Skill.objects.all()
        skill_data = [{"id": str(skill.id), "name": skill.name, "proficiency": skill.proficiency} for skill in skills]
        return Response(skill_data)
    
    def post(self, request):
        name = request.data.get("name")
        proficiency = request.data.get("proficiency")
        if not name or not proficiency:
            return Response({"error": "Name and proficiency are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        skill = Skill(name=name, proficiency=proficiency)
        skill.save()
        return Response({"id": str(skill.id), "name": skill.name, "proficiency": skill.proficiency}, status=status.HTTP_201_CREATED)

    def update(self, request, skill_id):
        skill = Skill.objects(id=skill_id).first()
        if not skill:
            return Response({"error": "Skill not found."}, status=status.HTTP_404_NOT_FOUND)
        
        name = request.data.get("name")
        proficiency = request.data.get("proficiency")
        if name:
            skill.name = name
        if proficiency:
            skill.proficiency = proficiency
        skill.save()
        return Response({"id": str(skill.id), "name": skill.name, "proficiency": skill.proficiency})
    
    def delete(self, request, skill_id):
        skill = Skill.objects(id=skill_id).first()
        if not skill:
            return Response({"error": "Skill not found."}, status=status.HTTP_404_NOT_FOUND)
        
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)