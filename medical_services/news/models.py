from django.db import models

class News(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    text = models.TextField(max_length=256, verbose_name='Содержание')
    is_published = models.BooleanField(verbose_name="Опубликована")


    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
