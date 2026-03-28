from django.shortcuts import render ,redirect

# Create your views here.


def home(request):
    if request.session.get("user_name"):
        return render(request, "home.html")
    else:
        return redirect("login")


def about(request):
    if request.session.get("user_name"):
        return render(request, "about.html")
    else:
        return redirect("login")


def contact(request):
    if request.session.get("user_name"):
        return render(request, "contact.html")
    else:
        return redirect("login")