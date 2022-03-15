# Generated by Django 4.0.2 on 2022-03-14 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_project', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=25)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(default=True, max_length=25, verbose_name='Описание')),
                ('start', models.DateField(verbose_name='Начало проекта')),
                ('end', models.DateField(verbose_name='Конец проекта')),
                ('developers', models.ManyToManyField(related_name='Разработчики', to=settings.AUTH_USER_MODEL)),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Руководитель', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_task', models.CharField(blank=True, max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.projects')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=250, verbose_name='Текст')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.comment', verbose_name='Родитель')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='main.projects', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
