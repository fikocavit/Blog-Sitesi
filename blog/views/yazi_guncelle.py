from blog.models import YazilarModel
from blog.forms import YaziEkleForm,YaziGuncelleForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
@login_required(login_url='/')
def yazi_guncelle(request, slug):
    yazi=get_object_or_404(YazilarModel,slug=slug, yazar=request.user)
    form=YaziGuncelleForm(request.POST or None, files=request.FILES or None,instance=yazi)
    if form.is_valid():
        form.save()
        return redirect('detay', slug=yazi.slug)
    
    
            
    
    
    
    return render(request, 'pages/yazi-ekle.html',context={
        'form' : form
    })
    