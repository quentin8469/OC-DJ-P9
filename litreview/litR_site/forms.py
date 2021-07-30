from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import RadioSelect, Textarea, TextInput

from .models import Ticket, Review, UserFollows


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
        labels = {
            "title": "Titre",
            "description": "Description",
            "image": "Image"
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        labels = {
            "rating": "Note",
            "headline": "Titre",
            "body": "Commentaire",
        }
        widgets = {
            "rating": RadioSelect(
                choices=[(0, "- 0"), (1, "- 1"), (2, "- 2"), (3, "- 3"), (4, "- 4"), (5, "- 5")]),
            "body": Textarea(),
            "headline": TextInput()
        }


class UserFollowForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ['user', 'followed_user']
