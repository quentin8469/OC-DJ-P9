from django import forms
from .models import Ticket


class NewUserForm(forms.Form):
    user_name = forms.CharField(max_length=8)
    password = forms.CharField(max_length=6, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=6, widget=forms.PasswordInput())

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get("confirm_password")
        password = self.cleaned_data.get("password")
        if confirm_password != password:
            raise forms.ValidationError("mot de passe different")
        return confirm_password


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']
        labels = {"title": "Titre",
                  }
