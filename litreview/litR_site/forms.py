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
        fields = ['title', 'description', 'image', 'user']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']



'''
class NewUserForm(forms.Form):
    """"""
    username = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    password1 = forms.CharField(max_length=6, widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe"}))
    password2 = forms.CharField(max_length=6, widget=forms.PasswordInput(attrs={"placeholder": "Confirmez votre mot de passe"}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get("confirm_password")
        password = self.cleaned_data.get("password")
        if confirm_password != password:
            raise forms.ValidationError("mot de passe different")
        return confirm_password
'''
