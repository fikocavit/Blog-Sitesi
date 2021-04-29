from django.contrib.auth.forms import UserChangeForm
from account.models import CustomUserModel


class ProfilGuncellemeForm(UserChangeForm):
    password=None
    class Meta:
        model=CustomUserModel
        fields=['username','email','last_name','first_name','avatar']