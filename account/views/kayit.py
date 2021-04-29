from account.forms import KayitForm
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
def kayit(request):
    if request.method=="POST":
        form=KayitForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('anasayfa')
            
            
    else:
        form=KayitForm()
    return render(request, 'pages/kayit.html',context={
        'form': form
    })
    