from blog.views import anasayfa,kategori,yazilar,detay,iletisim

from django.urls import path


urlpatterns = [
    path('', anasayfa,name='anasayfa'),
    path('kategori/<slug:kategoriSlug>', kategori,name='kategori'),
    path('yazilarim/', yazilar,name='yazilarim'),
    path('detay/<slug:slug>', detay,name='detay'),
    path('iletisim/',iletisim,name='iletisim')
]