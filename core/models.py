from django.contrib.auth.models import User
from django.db import models


class Technologies(models.Model):
    """
    Технологии
    """
    title = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.title


class UserPoll(User):
    """
    Анкета
    """
    experience = models.PositiveIntegerField(
        verbose_name='Опыт в программировании',
        default=0
    )

    age = models.PositiveIntegerField()

    technologies = models.ManyToManyField(
        Technologies,
        verbose_name='Технологии, которые я знаю',
        related_name='tech'
    )
    explore_technologies = models.ManyToManyField(
        Technologies,
        verbose_name='Технологии, которые хочу выучить',
        related_name='exp_tech'
    )
    is_mentor = models.BooleanField(
        verbose_name='Готов быть ментором',
        default=False
    )
    search_mentor = models.BooleanField(
        verbose_name='В поиске ментора',
        default=False
    )

    def __str__(self):
        return self.email


class Request(models.Model):
    """
    Заявка на поиск собеседника/ментора
    """
    title = models.CharField(
        max_length=255
    )

    tech = models.ForeignKey(
        Technologies,
        on_delete=models.CASCADE,
        related_name='techno'
    )

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='creator'
    )

    search_mentor = models.BooleanField(
        default=False
    )

    pair = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='pair'
    )

    def __str__(self):
        return self.title


class Offer(models.Model):
    """
    Предложение на менторство
    """
    request = models.ForeignKey(
        Request,
        on_delete=models.CASCADE,
        related_name='req'
    )

    who = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='who'
    )
    comments = models.CharField(
        max_length=255
    )

    accept = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.comments
