from django.db import models
from django.contrib.auth.models import User


class Photography(models.Model):
    photo = models.ImageField(null=False, blank=False, upload_to='photo', verbose_name="Фото")
    caption = models.CharField(max_length=500, null=False, blank=False, verbose_name="Подпись")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="photo",
                               verbose_name="Автор")





