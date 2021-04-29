from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUserModel


class KayitForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=[
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]