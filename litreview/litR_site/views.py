from django.shortcuts import render
from .forms import NewUserForm


def index(request):
    return render(request, "index.html")


def signup(request):
    form = NewUserForm()
    return render(request, "signup.html", {"form": form})


def flux(request):
    return render(request, "flux.html")


def follow_users(request):
    return render(request, "follow_users.html")


def create_ticket(request):
    return render(request, "create_ticket.html")


def create_critics(request):
    return render(request, "create_critics.html")


def answer_to_critic(request):
    return render(request, "answer_to_critic.html")


def show_own_critics(request):
    return render(request, "show_own_critics.html")


def edit_own_critics(request):
    return render(request, "show_own_critics.html")


def edit_own_ticket(request):
    return render(request, "edit_own_ticket.html")

