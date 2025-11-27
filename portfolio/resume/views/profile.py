from django.shortcuts import render



def profile_view(request):
    context = {"data": "Gfg is the best"}
    return render(request, "profile.html", context)