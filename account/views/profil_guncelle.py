from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from account.forms import ProfilGuncellemeForm
from django.contrib import messages
@login_required(login_url='/')
def profil_guncelle(request):
    if request.method=="POST":
        form=ProfilGuncellemeForm(request.POST,files=request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profil Basariyla Guncellendi")
            return redirect('profil-guncelleme')
    else:
        form=ProfilGuncellemeForm(instance=request.user)
    return render(request, 'pages/profil-guncelleme.html' ,context={
        'form' : form
    })