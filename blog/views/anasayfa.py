from django.shortcuts import render
from blog.models import YazilarModel

def anasayfa(request):
    yazilar=YazilarModel.objects.order_by("-id")
    return render(request, 'pages/anasayfa.html',context={
        'yazilar' : yazilar
    })
    