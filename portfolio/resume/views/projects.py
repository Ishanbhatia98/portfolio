from django.shortcuts import render

from resume.model.skill import Skill
from resume.model.school import School
from resume.model.work_ex import WorkExperience
from resume.model.certificate import Certificate
from resume.model.project import Project
def generate_project_context():
    projects = Project.objects.all()
    context = {
        "projects": projects,
        
    }
    return context


def project_view(request):
    return render(request, "projects.html", generate_project_context())