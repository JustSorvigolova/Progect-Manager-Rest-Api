from django.db import models
from django.contrib.auth.models import AbstractUser


class Supervisor(models.Model):
    """ Руководитель проекта """
    Lname = models.CharField(max_length=25)
    Fname = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'

    def __str__(self):
        return self.Lname


class Developers(models.Model):
    """ Разработчики проекта """
    Role_choice = (
        ('F', 'Front-End'),
        ('B', 'Back-End'),
        ('FS', 'Full-Stack')
    )
    Lname = models.CharField(max_length=25)
    Fname = models.CharField(max_length=25)
    role = models.CharField(max_length=15, choices=Role_choice)

    def __str__(self):
        return self.Lname

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'


class Tasks(models.Model):
    """ Задачи проекта """

    title_task = models.CharField(max_length=50, blank=True,)

    def __str__(self):
        return self.title_task

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Projects(models.Model):
    """  Проект """
    title = models.CharField(max_length=25)
    status = models.BooleanField(default=False)
    supervisor = models.ForeignKey(Supervisor, related_name='projects', on_delete=models.CASCADE)
    developers = models.ManyToManyField(Developers, related_name='developer')
    task = models.ManyToManyField(Tasks)
    start = models.DateField(auto_now_add=True)
    end = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Comment(models.Model):
    """ Комментарии """
    project = models.ForeignKey(Projects, verbose_name="проект", on_delete=models.CASCADE, related_name="comment")
    text = models.TextField("Текст", max_length=250)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комментарии'