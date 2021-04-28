from blog.views import anasayfa

from django.urls import path


urlpatterns = [
    path('', anasayfa,name='anasayfa'),
]