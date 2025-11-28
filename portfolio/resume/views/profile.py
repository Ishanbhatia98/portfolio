from django.shortcuts import render

from pprint import pprint





from resume.model.skill import Skill
from resume.model.school import School
from resume.model.work_ex import WorkExperience
from resume.model.certificate import Certificate
from resume.model.project import Project
def generate_profile_context():
    skills = Skill.objects.all()
    education = School.objects.all().order_by('-end_date')
    work_experiences = WorkExperience.objects.all().order_by('-end_date')
    certifications = Certificate.objects.all()
    projects = Project.objects.all()
    context = {
        "skills": skills,
        "education": education,
        "experience": work_experiences,
        "certifications": certifications,
        "projects": projects,
        
    }
    return context

def profile_view(request):
    return render(request, "profile.html", generate_profile_context())