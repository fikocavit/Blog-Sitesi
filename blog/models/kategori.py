from django.db import models
from autoslug import AutoSlugField # pip install django-autoslug

class KategoriModel(models.Model):
    isim=models.CharField(max_length=50,blank=False,null=False) # blank ve null False olma sebebi doldurulmasi gerekmesi
    slug=AutoSlugField(populate_from='isim',unique=True)# Her ismin bir slug i olmasi lazim unique dedigimiz sey ise isimler birbirine benzememesi icin eklenmistir.
    
    
    class Meta:
        db_table="Kategoriler"
        verbose_name_plural="Kategoriler"
    
    def __str__(self):
        return self.isim
        
        
        
# www.blog.com/"kategori ismi"/ gibi