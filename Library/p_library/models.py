from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class Author(models.Model):
    full_name = models.TextField('Полное имя')
    birth_year = models.SmallIntegerField('Год рождения')
    country = models.CharField('Страна', max_length=2)
    cover = models.ImageField(upload_to='authors_covers', null=True, blank=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse_lazy('p_library:author', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Publisher(models.Model):
    name = models.TextField('Полное имя')
    city = models.TextField('Город')
    cover = models.ImageField(upload_to='publishers_covers', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('p_library:publisher', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField('Название книги')
    description = models.TextField('Описание')
    year_release = models.SmallIntegerField('Год издания', default=0)
    copy_count = models.PositiveSmallIntegerField('Количество копий', default=1)
    price = models.FloatField('Цена', default=0.00)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, blank=True)
    friend = models.ForeignKey('Friend', on_delete=models.SET_NULL, null=True, related_name='friends', blank=True)
    cover = models.ImageField(upload_to='book_covers', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('p_library:book', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['title']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Friend(models.Model):
    full_name = models.fields.CharField('Полное имя', max_length=100)
    cover = models.ImageField(upload_to='readers_covers', null=True, blank=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse_lazy('p_library:reader', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Друг-читатель'
        verbose_name_plural = 'Друзья-читатели'



class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.SmallIntegerField(blank=True, default=None, null=True)
    phone = models.TextField(blank=True, default=None, null=True)
    birthday = models.DateTimeField(blank=True, default=None, null=True)
