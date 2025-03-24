from django.db import models

# Create your models here.

class Articles(models.Model):
    #title, anons, full_text, date
    title = models.CharField('Назва новини', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Новина')
    date = models.DateTimeField('Дата публікації')
    
    def __str__(self):
        return f"Новина: {self.title}"
    
    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'