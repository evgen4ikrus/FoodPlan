# Generated by Django 3.2.15 on 2022-09-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория блида',
                'verbose_name_plural': 'Категории блюд',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('instruction', models.TextField(blank=True, verbose_name='Инструкция приготовления')),
                ('ingredients', models.TextField(blank=True, verbose_name='Ингридиенты')),
                ('price', models.FloatField(blank=True, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('category', models.ManyToManyField(related_name='recipes', to='recipes.Category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegramm_id', models.IntegerField(verbose_name='Telegram ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='disliked_users', to='recipes.Recipe', verbose_name='Не понравившееся рецерт')),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_users', to='recipes.Recipe', verbose_name='Понравившееся рецерты')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]