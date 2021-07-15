
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import NewUserForm, NewTicketForm, ReviewForm
from django.contrib.auth.decorators import login_required

from .models import Ticket

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


@login_required(login_url='home')
def follow_users(request):
    """
    :param request:
    :return:
    """
    return render(request, "follow_users.html")


@login_required(login_url='home')
def create_ticket(request):
    """
    :param request:
    :return:
    """

    if request.method == "POST":
        form = NewTicketForm(request.POST, request.FILES)
        if form.is_valid():
            n_ticket = form.save(commit=False)
            n_ticket.image = form.cleaned_data['image']
            n_ticket.user = request.user
            n_ticket.save()
            return redirect('flux')
    else:
        form = NewTicketForm()
    return render(request, "create_ticket.html", {"form": form})


@login_required(login_url='home')
def create_critics(request):
    """
    :param request:
    :return:
    """
    print('bob0')
    if request.method == "POST":
        ticketform = NewTicketForm(request.POST, request.FILES)
        criticform = ReviewForm(request.POST)
        print('bob 1')
        if ticketform.is_valid() and criticform.is_valid():
            ticketform.save()
            criticform.save()
            '''
            critic = criticform.save(commit=False)
            ticket = ticketform.save(commit=False)
            print('bob2')
            critic.user = request.user
            ticket.user = request.user
            ticket.save()
            print('bob3')
            critic.ticket = ticket
            critic.save()
            print('bob4')
            '''
            return redirect('flux')
    else:
        print('bob echec')
        ticketform = NewTicketForm()
        criticform = ReviewForm()

    return render(request, "create_critics.html", {"ticketform": ticketform, "criticform": criticform})


@login_required(login_url='home')
def answer_to_critic(request):
    """
    :param request:
    :return:
    """
    return render(request, "answer_to_critic.html")


@login_required(login_url='home')
def show_own_critics(request):
    """
    :param request:
    :return:
    """
    return render(request, "show_own_critics.html")


@login_required(login_url='home')
def edit_own_critics(request):
    """
    :param request:
    :return:
    """
    return render(request, "show_own_critics.html")


@login_required(login_url='home')
def edit_own_ticket(request):
    """
    :param request:
    :return:
    """
    return render(request, "edit_own_ticket.html")
