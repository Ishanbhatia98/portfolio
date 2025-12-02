from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from resume.model.work_ex import WorkExperience, LineItem


class WorkExCRUDAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        work_experiences = WorkExperience.objects.all().order_by('-start_date')
        work_ex_data = [{
            "id": str(work_ex.id),
            "org": work_ex.org,
            "role": work_ex.role,
            "start_date": work_ex.start_date,
            "end_date": work_ex.end_date,
            "description": [
                item.to_dict() for item in work_ex.description
            ]
        } for work_ex in work_experiences]
        return Response(work_ex_data)
    
    def post(self, request):
        org = request.data.get("org")
        role = request.data.get("role")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        description = [
            LineItem(content=item) for item in request.data.get("description", [])
        ]
        
        if not org or not role or not start_date:
            return Response({"error": "org name, role, and start date are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        work_ex = WorkExperience(
            org=org,
            role=role,
            start_date=start_date,
            end_date=end_date,
            description=description
        )
        work_ex.save()
        return Response({
            "id": str(work_ex.id),
            "org": work_ex.org,
            "role": work_ex.role,
            "start_date": work_ex.start_date,
            "end_date": work_ex.end_date,
            "description": [
                item.to_dict() for item in work_ex.description
            ]
        }, status=status.HTTP_201_CREATED)
    
    def put(self, request, work_ex_id):
        work_ex = WorkExperience.objects(id=work_ex_id).first()
        if not work_ex:
            return Response({"error": "Work experience not found."}, status=status.HTTP_404_NOT_FOUND)
        
        org = request.data.get("org")
        role = request.data.get("role")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        description = request.data.get("description")
        
        if org:
            work_ex.org = org
        if role:
            work_ex.role = role
        if start_date:
            work_ex.start_date = start_date
        if end_date:
            work_ex.end_date = end_date
        if description:
            new_description = []
            for item in description:
                line_item = LineItem(content=item)
                line_item.save()
                new_description.append(line_item)
                
            work_ex.description = new_description
        
        work_ex.save()
        return Response({
            "id": str(work_ex.id),
            "org": work_ex.org,
            "role": work_ex.role,
            "start_date": work_ex.start_date,
            "end_date": work_ex.end_date,
           "description": [
                item.to_dict() for item in work_ex.description
            ]
        })
    
    def delete(self, request, work_ex_id):
        work_ex = WorkExperience.objects(id=work_ex_id).first()
        if not work_ex:
            return Response({"error": "Work experience not found."}, status=status.HTTP_404_NOT_FOUND)
        
        work_ex.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    