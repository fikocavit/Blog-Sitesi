from django.shortcuts import render,get_object_or_404,redirect
from blog.models import YazilarModel
from blog.forms import YorumEkleForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def detay(request, slug):
    yazi=get_object_or_404(YazilarModel, slug=slug)
    yorumlar=yazi.yorum.all()
    if request.method=="POST":
        yorum_ekle_form=YorumEkleForm(request.POST)
        if yorum_ekle_form.is_valid():
            yorum=yorum_ekle_form.save(commit=False)
            yorum.yazar=request.user
            yorum.yazi=yazi
            yorum.save()
            return redirect('detay', slug=yazi.slug)
    yorum_ekle_form=YorumEkleForm()
    return render(request, 'pages/detay.html',context={
        'yazi' : yazi,
        'yorumlar' : yorumlar,
        'yorum_ekle_form' : yorum_ekle_form,
    })
    