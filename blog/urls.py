from blog.views import anasayfa,kategori

from django.urls import path


urlpatterns = [
    path('', anasayfa,name='anasayfa'),
    path('kategori/<slug:kategoriSlug>', kategori,name='kategori'),
]