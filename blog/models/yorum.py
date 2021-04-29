from django.db import models
from django.contrib.auth.models import User
from blog.models import YazilarModel


class YorumlarModel(models.Model):
    yazi=models.ForeignKey(YazilarModel,on_delete=models.CASCADE,related_name='yorumlar')
    yazar=models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE,related_name='yorum')
    yorum=models.TextField()
    olusturma_tarihi=models.DateTimeField(auto_now_add=True)
    duzenleme_tarihi=models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table="Yorumlar"
        verbose_name="Yorum"
        verbose_name_plural="Yorumlar"
        
        
    def __str__(self):
        return self.yazar.username