from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import (
    RangeOperators,
)
from django.db import models
from django.contrib.postgres.fields import DateRangeField


class Administrator(models.Model):
    """ Администратор проекта """

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'


class Supervisor(models.Model):
    """ Руководитель проекта """
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'


class Workers(models.Model):

    """ Разработчики проекта """
    Role_choice = (
        ('F', 'Front-End'),
        ('B', 'Back-End'),
    )
    name = models.CharField(max_length=25)
    role = models.CharField(max_length=15, choices=Role_choice)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'


class Tasks(models.Model):
    """ Задачи проекта """
    task = models.CharField(max_length=50)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Projects(models.Model):
    """  Проект """
    title = models.CharField(max_length=25)
    status = models.BooleanField(default=False)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    workers = models.ManyToManyField(Workers)
    date_range = DateRangeField()
    admin = models.OneToOneField(Administrator, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            ExclusionConstraint(
                name='exclude_overlap',
                expressions=[
                    ('date_range', RangeOperators.OVERLAPS),
                ],
            )]
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


