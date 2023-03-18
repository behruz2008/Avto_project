from django.db import models



class Kategoriya(models.Model):
    nomi = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.nomi
    
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        
        
class Avtomobil(models.Model):
    kategoriya = models.ForeignKey(Kategoriya, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='avto_rasmlar')
    nomi = models.CharField(max_length=200)
    yil = models.IntegerField()
    manzil = models.CharField(max_length=200)
    modeli = models.CharField(max_length=100)
    rang = models.CharField(max_length=100)
    pozitsiya = models.IntegerField()
    egasi = models.CharField(max_length=100)
    tel = models.IntegerField()
    izoh = models.TextField()
    
    def __str__(self):
        return self.nomi
    
    
    class Meta:
        verbose_name = 'Avtomobil'
        verbose_name_plural = 'Avtomobillar'
    
    
    
