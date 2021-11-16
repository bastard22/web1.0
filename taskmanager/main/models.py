from django.db import models


class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('HELP')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'QUEST'
        verbose_name_plural = 'QUESTS'

class nenad(models.Model):
    name = models.CharField(max_length=50)
    nenad_main_img = models.ImageField(upload_to='images/')