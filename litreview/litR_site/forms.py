from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Ticket, Review


class NewUserForm(UserCreationForm):
    """

    """

    class Meta:
        """

        """
        model = User
        fields = ("username", "password1", "password2")


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
