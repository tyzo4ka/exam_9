from django.db import models
from django.contrib.auth.models import User


class Photography(models.Model):
    photo = models.ImageField(null=False, blank=False, upload_to='photo', verbose_name="Фото")
    caption = models.CharField(max_length=500, null=False, blank=False, verbose_name="Подпись")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    photo_author = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="photo",
                               verbose_name="Автор фотографии")

    def __str__(self):
        return self.caption


class Comments(models.Model):
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    photography = models.ForeignKey("webapp.Photography", related_name="comments", on_delete=models.CASCADE,
                                    verbose_name="Фотография")
    comments_author = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="comments",
                               verbose_name="Автор комментария")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.text










