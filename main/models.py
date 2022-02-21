from django.db import models


class Tasks(models.Model):
    """ Задачи проекта """
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


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


class Projects(models.Model):
    """  Проект """
    title = models.CharField(max_length=25)
    status = models.BooleanField(default=False)
    supervisor = models.CharField(max_length=25)
    start = models.DateField()
    end = models.DateField()
    admin = models.CharField(max_length=25)
    description = models.TextField(max_length=150)
    workers = models.ManyToManyField(Workers)
    task = models.ManyToManyField(Tasks)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


