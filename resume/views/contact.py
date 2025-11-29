
from django.shortcuts import render, redirect
from django.contrib import messages
from resume.model.contact_message import ContactMessage
from mongoengine import get_db

def contact_view(request):
    context = {"data": "Gfg is the best"}
    return render(request, "contact.html", context)




def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        number = request.POST.get("number", "").strip()
        message_text = request.POST.get("message", "").strip()

        if not name:
            messages.error(request, "Name is required.")
            return redirect("contact")
        print('yoooo')
        # Save to MongoDB
        contact = ContactMessage(
            name=name,
            email=email,
            number=number,
            message=message_text
        )
        contact.save()
        #get db name
        print(ContactMessage._get_db().name)
        db = get_db(alias='default')
        print(db.name)  # S
        print('yoooo 22')
        messages.success(request, "Thank you! Your message has been sent.")
        return redirect("contact")

    return redirect("contact")