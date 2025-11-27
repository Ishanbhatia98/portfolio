from django.shortcuts import render



def project_view(request):
    context = {"data": "Gfg is the best"}
    return render(request, "projects.html", context)