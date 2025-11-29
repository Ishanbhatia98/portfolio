from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from uauth.model.user import User


def login_view(request):
    context = {"data": "Gfg is the best"}

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        hashed_password = make_password(password)
        user = User.objects(email=username).first()
        print(user.email if user else "No user found")
        if user and check_password(password, hashed_password):
            context["message"] = "Login successful!"
            return render(request, "home.html", context)

        messages.error(request, "Invalid username or password.")
        context["message"] = "Invalid username or password."
        return render(request, "login.html", context)

    return render(request, "login.html", context)