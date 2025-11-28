from django.shortcuts import render



def signup_view(request):
    context = {"data": "Gfg is the best"}
    return render(request, "signup.html", context)

