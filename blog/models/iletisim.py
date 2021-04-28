from django.db import models



class IletisimModel(models.Model):
    email=models.EmailField(max_length=256,blank=False,null=False)
    isim_soyisim=models.CharField(max_length=50,blank=False,null=False)
    mesaj=models.TextField()
    gonderme_tarihi=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table="Iletisim"
        
