from django.contrib import admin
from blog.models import KategoriModel,YazilarModel,YorumlarModel,IletisimModel
# Register your models here.
@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields=['baslik','yazar']
    list_display=['baslik','yazar','olusturma_tarihi']
    
@admin.register(YorumlarModel)
class YorumlarAdmin(admin.ModelAdmin):
    search_fields=['yorum','yazar']
    list_display=['yorum','yazar','olusturma_tarihi']
    
@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    search_fields=['email','isim_soyisim']
    list_display=['email','isim_soyisim','gonderme_tarihi']


admin.site.register(KategoriModel)