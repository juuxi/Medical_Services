from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    short_description = models.CharField(max_length=64, verbose_name='Сокращенное описание')
    description = models.TextField(max_length=256, verbose_name='Описание')
    cost = models.IntegerField(verbose_name="Стоимость")
    duration_minutes = models.SmallIntegerField(verbose_name="Продолжительность")
    image = models.ImageField('Фото', upload_to='service_images', blank=True)
    is_provided = models.BooleanField(verbose_name="Предоставляется")
    is_key = models.BooleanField(verbose_name="Ключевая")


    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name
