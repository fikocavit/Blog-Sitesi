from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
@login_required(login_url='/')
def sifre_degistir(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user , request.POST)
        if form.is_valid():
            kullanici=form.save()
            update_session_auth_hash(request, kullanici)
            return redirect('anasayfa')
    else:
        form=PasswordChangeForm(request.user)
    return render(request, 'pages/sifre-degistir.html' ,context={
        'form' : form
    })