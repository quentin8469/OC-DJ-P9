from django import forms


class NewUserForm(forms.Form):
    user_name = forms.CharField(max_length=8)
    password = forms.CharField(max_length=6)
    confirm_password = forms.CharField(max_length=6)

