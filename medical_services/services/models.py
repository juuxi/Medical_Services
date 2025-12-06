from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    cost = models.IntegerField(verbose_name="Стоимость")
    duration_minutes = models.SmallIntegerField(verbose_name="Продолжительность")
    is_provided = models.BooleanField(verbose_name="Предоставляется")


    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name
