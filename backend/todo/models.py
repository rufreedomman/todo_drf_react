from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата и время создания')
    completed = models.BooleanField(default=False,
                                    verbose_name='Флаг выполнения')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь')

    class Meta:
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title
