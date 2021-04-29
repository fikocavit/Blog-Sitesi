from django.shortcuts import render,get_object_or_404
from blog.models import YazilarModel,KategoriModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def yazilar(request):
    yazilar=request.user.yazilar.order_by("-id")
    return render(request, 'pages/yazilarim.html',context={
        'yazilar' : yazilar,
    })
    