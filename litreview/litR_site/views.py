
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import NewUserForm, NewTicketForm
from django.contrib.auth.decorators import login_required
'''
    Kevin
    k1e2v3i4n5
'''


def index(request):
    """
    :param request:
    :return:
    """

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('flux')

    return render(request, "index.html")


def logout_user(request):
    logout(request)
    return redirect('home')

def signup(request):
    """
    :param request:
    :return:
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewUserForm()
    return render(request, "signup.html", {"form": form})


@login_required(login_url='home')
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
