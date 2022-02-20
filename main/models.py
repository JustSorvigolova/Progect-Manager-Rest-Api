from abc import ABC
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import (
    DateTimeRangeField,
    RangeBoundary,
    RangeOperators,
)
from django.db import models
from django.db.models import Func, Q


class Administrator(models.Model):
    """ Руководитель проекта """

    name = models.CharField(max_length=25)


class Supervisor(models.Model):
    """ Руководитель проекта """

    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Задачи'


class Workers(models.Model):

    """ Разработчики проекта """
    Role_choice = (
        ('F', 'Front-End'),
        ('B', 'Back-End'),
    )
    name = models.CharField(max_length=25)
    role = models.CharField(max_length=15, choices=Role_choice)

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'


class TsTzRange(Func, ABC):
    function = 'TSTZRANGE'
    output_field = DateTimeRangeField()


class Tasks(models.Model):
    """ Задачи проекта """

    task = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Projects(models.Model):
    """  Проект """

    title = models.CharField(max_length=25)
    status = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    workers = models.ManyToManyField(Workers, on_delete=models.CASCADE)
    admin = models.OneToOneField(Administrator, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            ExclusionConstraint(
                name='exclude_overlapping_reservations',
                expressions=(
                    (TsTzRange('start_date', 'end_date', RangeBoundary()), RangeOperators.OVERLAPS),
                    ('room', RangeOperators.EQUAL),
                ),
                condition=Q(cancelled=False),
            ),
        ]
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


