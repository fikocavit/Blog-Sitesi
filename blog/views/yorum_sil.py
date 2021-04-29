from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from blog.models import YorumlarModel

@login_required(login_url='/')
def yorum_sil(request,id):
    yorum=get_object_or_404(YorumlarModel, id=id)
    if yorum.yazar == request.user or request.user==yorum.yazi.yazar:
        yorum.delete()
        
        return redirect('detay', slug = yorum.yazi.slug)
    
    return redirect('anasayfa')