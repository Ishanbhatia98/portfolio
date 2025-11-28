from django.shortcuts import render



def password_reset_view(request):
    context = {"data": "Gfg is the best"}
    return render(request, "password_reset.html", context)

