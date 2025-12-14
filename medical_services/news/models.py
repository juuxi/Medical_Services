from django.db import models

class News(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    short_text = models.TextField(max_length=64, 
                                  verbose_name='Сокращенное содержание')
    text = models.TextField(max_length=256, verbose_name='Содержание')
    image = models.ImageField('Фото', upload_to='news_images', blank=True)
    is_published = models.BooleanField(verbose_name="Опубликована")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено')


    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
