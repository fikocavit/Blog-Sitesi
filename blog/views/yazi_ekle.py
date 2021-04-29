from blog.models import YazilarModel
from blog.forms import YaziEkleForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
@login_required(login_url='/')
def yazi_ekle(request):
    form=YaziEkleForm(request.POST or None,files=request.FILES or None)
    if form.is_valid():
        yazi=form.save(commit=False)
        yazi.yazar=request.user
        yazi.save()
        return redirect('yazilarim')
            
    
    
    
    return render(request, 'pages/yazi-ekle.html',context={
        'form' : form
    })
    