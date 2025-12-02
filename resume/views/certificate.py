from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from resume.model.certificate import Certificate, LineItem


class CertificateCRUDAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        certificates = Certificate.objects.all().order_by('-date')
        certificate_data = [{
            "id": str(certificate.id),
            "title": certificate.title,
            "issuer": certificate.issuer,
            "date": certificate.date,
           "description": [
                item.to_dict() for item in certificate.description
            ],
            "link": certificate.link
        } for certificate in certificates]
        return Response(certificate_data)

    def post(self, request):
        title = request.data.get("title")
        issuer = request.data.get("issuer", "")
        date = request.data.get("date")
        description = [LineItem(item) for item in request.data.get("description", [])]
        link = request.data.get("link", "")

        if not title or not date:
            return Response({"error": "Title and date are required."}, status=status.HTTP_400_BAD_REQUEST)

        certificate = Certificate(
            title=title,
            issuer=issuer,
            date=date,
            description=description,
            link=link
        )
        certificate.save()
        return Response({
            "id": str(certificate.id),
            "title": certificate.title,
            "issuer": certificate.issuer,
            "date": certificate.date,
           "description": [
                item.to_dict() for item in certificate.description
            ],
            "link": certificate.link
        }, status=status.HTTP_201_CREATED)

    def put(self, request, certificate_id):
        certificate = Certificate.objects(id=certificate_id).first()
        if not certificate:
            return Response({"error": "Certificate not found."}, status=status.HTTP_404_NOT_FOUND)

        title = request.data.get("title")
        issuer = request.data.get("issuer")
        date = request.data.get("date")
        description = request.data.get("description")
        link = request.data.get("link")

        if title:
            certificate.title = title
        if issuer:
            certificate.issuer = issuer
        if date:
            certificate.date = date
        if description:
            certificate.description = [LineItem(item) for item in request.data.get("description", [])]
        if link:
            certificate.link = link

        certificate.save()
        return Response({
            "id": str(certificate.id),
            "title": certificate.title,
            "issuer": certificate.issuer,
            "date": certificate.date,
           "description": [
                item.to_dict() for item in certificate.description
            ],
            "link": certificate.link
        })

    def delete(self, request, certificate_id):
        certificate = Certificate.objects(id=certificate_id).first()
        if not certificate:
            return Response({"error": "Certificate not found."}, status=status.HTTP_404_NOT_FOUND)

        certificate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)