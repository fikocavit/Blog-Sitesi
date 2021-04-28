from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from blog.models import KategoriModel


class YazilarModel(models.Model):
    resmi=models.ImageField(upload_to='yazi_resim')
    baslik=models.CharField(max_length=50,blank=False,null=False)
    icerik=models.TextField()
    yazar=models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE,related_name='yazilar')
    olusturma_tarihi=models.DateTimeField(auto_now_add=True)
    duzenleme_tarihi=models.DateTimeField(auto_now=True)
    slug=AutoSlugField(populate_from='baslik',unique=True)
    kategoriler=models.ManyToManyField(KategoriModel,related_name='yazi')
    
    class Meta:
        db_table="Yazilar"
        verbose_name="Yazi"
        verbose_name_plural="Yazilar"
        
        
    def __str__(self):
        return self.baslik
    