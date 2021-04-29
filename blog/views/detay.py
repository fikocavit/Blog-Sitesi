from django.shortcuts import render,get_object_or_404
from blog.models import YazilarModel
def detay(request, slug):
    yazi=get_object_or_404(YazilarModel, slug=slug)
    yorumlar=yazi.yorum.all()
    return render(request, 'pages/detay.html',context={
        'yazi' : yazi,
        'yorumlar' : yorumlar
    })
    