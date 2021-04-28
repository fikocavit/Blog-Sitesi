from django.shortcuts import render


def anasayfa(request):
    return render(request, 'pages/anasayfa.html',context={})
    