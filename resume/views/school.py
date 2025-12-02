from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from resume.model.school import School, LineItem


class SchoolCRUDAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        schools = School.objects.all().order_by('-start_date')
        school_data = [{
            "id": str(school.id),
            "institution": school.institution,
            "degree": school.degree,
            "start_date": school.start_date,
            "end_date": school.end_date,
           "description": [
                item.to_dict() for item in school.description
            ],
            "location": school.location
        } for school in schools]
        return Response(school_data)
    
    def post(self, request):
        institution = request.data.get("institution")
        degree = request.data.get("degree")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        description = [
            LineItem(content=item) for item in request.data.get("description", [])
        ]
        location = request.data.get("location", "")
        
        if not institution or not degree or not start_date:
            return Response({"error": "Institution, degree, and start date are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        school = School(
            institution=institution,
            degree=degree,
            start_date=start_date,
            end_date=end_date,
            description=description,
            location=location
        )
        school.save()
        return Response({
            "id": str(school.id),
            "institution": school.institution,
            "degree": school.degree,
            "start_date": school.start_date,
            "end_date": school.end_date,
           "description": [
                item.to_dict() for item in school.description
            ],
            "location": school.location
        }, status=status.HTTP_201_CREATED)

    def put(self, request, school_id):
        school = School.objects(id=school_id).first()
        if not school:
            return Response({"error": "School not found."}, status=status.HTTP_404_NOT_FOUND)
        
        institution = request.data.get("institution")
        degree = request.data.get("degree")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        description = request.data.get("description")
        location = request.data.get("location")
        
        if institution:
            school.institution = institution
        if degree:
            school.degree = degree
        if start_date:
            school.start_date = start_date
        if end_date:
            school.end_date = end_date
        if description:
            school.description = [
                LineItem(content=item) for item in description
            ]
        if location:
            school.location = location
        school.save()
        return Response({
            "id": str(school.id),
            "institution": school.institution,
            "degree": school.degree,
            "start_date": school.start_date,
            "end_date": school.end_date,
           "description": [
                item.to_dict() for item in school.description
            ],
            "location": school.location
        })

    def delete(self, request, school_id):
        school = School.objects(id=school_id).first()
        if not school:
            return Response({"error": "School not found."}, status=status.HTTP_404_NOT_FOUND)
        
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    