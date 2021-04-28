from django.db import models
from blog.models import YazilarModel
from django.contrib.auth.models import User


class BegenilerModel(models.Model):
    yazi=models.ForeignKey(YazilarModel,on_delete=models.CASCADE,related_name='begeniler')
    yazar=models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE,related_name='begeni')
    olusturma_tarihi=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table="Begeniler"
        verbose_name="Begeni"
        verbose_name_plural="Begeniler"