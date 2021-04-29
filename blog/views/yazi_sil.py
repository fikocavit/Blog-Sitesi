from blog.models import YazilarModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404


def yazi_sil(request, slug):
    yazi=get_object_or_404(YazilarModel, slug=slug, yazar=request.user).delete()
    return redirect('yazilarim')
    
    