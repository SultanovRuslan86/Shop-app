from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Head', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Full_text')
    date = models.DateTimeField('Data')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'