from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import NewUserForm, NewTicketForm, ReviewForm, UserFollowForm
from django.contrib.auth.decorators import login_required

from .models import Ticket, Review, UserFollows

'''
    Kevin
    k1e2v3i4n5
    bobill
    b1o2b3i4l5l6
    Rambo
    r1a2m3b4o5
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
    tickets = Ticket.objects.all()
    critiques = Review.objects.all()

    return render(request, "flux.html", {'tickets': tickets, 'critiques': critiques})


@login_required(login_url='home')
def follow_users(request):
    """
    :param request:
    :return:
    """

    users = User.objects.all()
    if request.method == "POST":
        username = request.POST.get("username")
        for user in users:
            if user.username == username:
                if user.username == request.user.username:
                    messages.info(request, "Cant following you")
                else:
                    user_follow = UserFollows(user=request.user, followed_user=user)
                    try:
                        user_follow.save()
                    except IntegrityError:
                        messages.info(request, "Username already followed")
                return redirect("follow")
        else:
            messages.info(request, "Username does not exist")
    form = UserFollowForm()
    try:
        users_following = UserFollows.objects.filter(user=request.user)
        users_follower = UserFollows.objects.filter(followed_user=request.user)
    except UserFollows.DoesNotExist:
        raise Http404("UserFollows does not exist")

    return render(request, "follow_users.html", {
        "form": form,
        "users_following": users_following,
        "users_follower": users_follower,
    })



    '''
    users = User.objects.all()
    if request.method == "POST":
        username = request.POST.get("username")
        for user in users:
            if user.username == request.user.username:
                erreur = ("pas possible")
            else:
                user_follow = UserFollows(user=request.user, followed_user=user)
                user_follow.save()
                return redirect('follow')

    form = UserFollowForm()
    usersfollows = UserFollows.objects.filter(user=request.user)
    followeds = UserFollows.objects.filter(followed_user=request.user)

    return render(request, "follow_users.html", {'form': form,
                                                'usersfollows': usersfollows,
                                                'followeds': followeds})
    '''

    '''
    users = User.objects.all()
    user = request.user
    usersfollows = UserFollows.objects.filter(user=user.id)
    followeds = UserFollows.objects.filter(followed_user=user.id)
    return render(request,"follow_users.html", {'usersfollows': usersfollows, 'followeds': followeds})
    if request.method == "GET":
        form = UserFollowForm()
        return render(request, "follow_users.html", {'form': form})
    
    return render(request, "follow_users.html", {'users': users})
    '''


@login_required(login_url='home')
def unfollow_user(request, id_follow):
    """
    """
    unfollow = UserFollows.objects.get(pk=id_follow)
    unfollow.delete()
    return redirect('follow')


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
    if request.method == "POST":
        form_crit = ReviewForm(request.POST)
        form_tik = NewTicketForm(request.POST, request.FILES)
        if form_crit.is_valid() and form_tik.is_valid():
            ticket = form_tik.save(commit=False)
            ticket.user = request.user
            ticket.save()
            critic = form_crit.save(commit=False)
            critic.user = request.user
            critic.ticket = ticket
            critic.save()
            return redirect('flux')
    else:
        form_crit = ReviewForm()
        form_tik = NewTicketForm()

    return render(request, "create_critics.html", {"form_crit": form_crit, "form_tik": form_tik, })


@login_required(login_url='home')
def answer_to_critic(request, ticket_id):
    """
    :param request:
    :return:
    """
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        form_crit = ReviewForm(request.POST)
        if form_crit.is_valid():
            critic = form_crit.save(commit=False)
            critic.user = request.user
            critic.ticket = ticket
            critic.save()
            return redirect('flux')
    else:
        form_crit = ReviewForm()
    return render(request, "answer_to_critic.html", {'ticket': ticket, 'form_crit': form_crit})


@login_required(login_url='home')
def show_own_critics(request):
    """
    :param request:
    :return:
    """
    user = request.user
    tickets = Ticket.objects.filter(user=user.id)
    critiques = Review.objects.filter(user=user.id)
    return render(request, "show_own_critics.html", {'tickets': tickets, 'critiques': critiques})


@login_required(login_url='home')
def edit_own_critics(request, review_id):
    """

    :param request:
    :param review_id:
    :return:
    """
    review = Review.objects.get(pk=review_id)
    ticket = review.ticket
    edit_review_form = ReviewForm(request.POST or None, instance=review)
    if edit_review_form.is_valid():
        edit_review_form.save()
        return redirect('show-critics')
    return render(request, "edit_own_critics.html", {'edit_review_form': edit_review_form, 'ticket': ticket})


@login_required(login_url='home')
def edit_own_ticket(request, ticket_id):
    """
    :param request:
    :param ticket_id:
    :return:
    """
    ticket = Ticket.objects.get(pk=ticket_id, user=request.user.id)
    edit_ticket_form = NewTicketForm(request.POST or None, request.FILES or None, instance=ticket)
    if edit_ticket_form.is_valid():
        ticket.image = edit_ticket_form.cleaned_data['image']
        edit_ticket_form.save()
        return redirect('show-critics')
    return render(request, "edit_own_ticket.html", {'edit_ticket_form': edit_ticket_form})


@login_required(login_url='home')
def del_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id, user=request.user.id)
    ticket.delete()
    return redirect('show-critics')


@login_required(login_url='home')
def del_review(request, review_id):
    review = Ticket.objects.get(pk=review_id, user=request.user.id)
    review.delete()
    return redirect('show-critics')
