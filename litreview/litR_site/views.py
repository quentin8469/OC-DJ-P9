
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import NewUserForm, NewTicketForm, ReviewForm
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
        form = NewTicketForm(request.POST)
        if form.is_valid():
            form.save()
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
        print('bob1')
        ticketform = NewTicketForm(request.POST)
        print('bob2')
        criticform = ReviewForm(request.POST)
        print('bob3')
        if ticketform.is_valid() and criticform.is_valid():
            critic = criticform.save(commit=False)
            ticket = ticketform.save(commit=False)
            print('bob4')
            ticket.save()
            print('bob5')
            critic.save()
            print('bob6')
            return redirect('flux')
    else:
        print('bob7')
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
