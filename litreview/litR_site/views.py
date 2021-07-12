from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from .forms import NewUserForm, NewTicketForm



def index(request):
    """
    :param request:
    :return:
    """
    return render(request, "index.html")


def signup(request):
    """
    :param request:
    :return:
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return render(request, "index.html")
    else:
        form = NewUserForm()
    return render(request, "signup.html", {"form": form})


def flux(request):
    """
    :param request:
    :return:
    """
    return render(request, "flux.html")


def follow_users(request):
    """
    :param request:
    :return:
    """
    return render(request, "follow_users.html")


def create_ticket(request):
    """
    :param request:
    :return:
    """
    if request.method == "POST":
        form = NewTicketForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = NewTicketForm()
    return render(request, "create_ticket.html", {"form": form})


def create_critics(request):
    """
    :param request:
    :return:
    """
    return render(request, "create_critics.html")


def answer_to_critic(request):
    """
    :param request:
    :return:
    """
    return render(request, "answer_to_critic.html")


def show_own_critics(request):
    """
    :param request:
    :return:
    """
    return render(request, "show_own_critics.html")


def edit_own_critics(request):
    """
    :param request:
    :return:
    """
    return render(request, "show_own_critics.html")


def edit_own_ticket(request):
    """
    :param request:
    :return:
    """
    return render(request, "edit_own_ticket.html")
