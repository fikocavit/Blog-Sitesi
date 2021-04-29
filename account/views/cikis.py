from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
@login_required(login_url='/')
def cikis(reqeust):
    logout(reqeust)
    return redirect('anasayfa')