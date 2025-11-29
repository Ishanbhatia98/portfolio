from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from uauth.model.user import User


def signup_view(request):
    context = {"data": "Gfg is the best"}

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        existing_user = User.objects(email=email).first()
        if existing_user:
            messages.error(request, "Email is already registered.")
            return redirect("signup")

        # hash the password
        hashed_password = make_password(password)

        # save the hashed pwd
        user = User(email=email, password=hashed_password)
        user.save()

        messages.success(request, "Thank you! Your message has been sent.")
        return redirect("home")

    return render(request, "signup.html", context)
