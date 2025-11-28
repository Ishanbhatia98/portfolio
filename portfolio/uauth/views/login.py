from django.shortcuts import render



def login_view(request):
    context = {"data": "Gfg is the best"}
    return render(request, "login.html", context)

