from blog.views import anasayfa,kategori,yazilar,detay,iletisim,yazi_ekle,yazi_guncelle,yazi_sil,yorum_sil

from django.urls import path


urlpatterns = [
    path('', anasayfa,name='anasayfa'),
    path('kategori/<slug:kategoriSlug>', kategori,name='kategori'),
    path('yazilarim/', yazilar,name='yazilarim'),
    path('detay/<slug:slug>', detay,name='detay'),
    path('iletisim/',iletisim,name='iletisim'),
    path('yazi-ekle/',yazi_ekle,name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>', yazi_guncelle,name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>', yazi_sil,name='yazi-sil'),
    path('yorum-sil/<int:id>', yorum_sil,name='yorum-sil'),
]