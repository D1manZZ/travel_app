from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Cities(models.Model):
    city = models.CharField('Город', max_length=50, unique=True)
    description = models.TextField('Описание города')
    photo = models.ImageField(upload_to='photos')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = "Города"

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return reverse('city', kwargs={'pk': self.id})


class Planes(models.Model):
    plain_code = models.CharField('Код рейса', max_length=20, unique=True)
    plain_start = models.ForeignKey(Cities, related_name="plain_start_set", verbose_name='Место старта', on_delete=models.CASCADE)
    plain_end = models.ForeignKey(Cities, related_name='plain_end_set', verbose_name="Конечная остановка", on_delete=models.CASCADE)
    trip_time = models.PositiveIntegerField('Время в пути')

    def clean(self):
        if self.plain_start == self.plain_end:
            raise ValidationError('Неправильный маршрут')
        qs = Planes.objects.filter(plain_start=self.plain_start, plain_end=self.plain_end, trip_time=self.trip_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Такой маршрут уже есть')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.plain_code

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'

    def get_absolute_url(self):
        return reverse('flight', kwargs={'pk': self.pk})


class Routes(models.Model):
    route_name = models.CharField('имя маршрута', max_length=30, unique=True)
    route_start = models.ForeignKey(Cities, related_name='Начало_маршрута', on_delete=models.CASCADE)
    route_end = models.ForeignKey(Cities, related_name='Конец_маршрута', on_delete=models.CASCADE)
