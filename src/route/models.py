from django.db import models


class Cities(models.Model):
    city = models.CharField('Город', max_length=50)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = "Города"

    def __str__(self):
        return self.city


class Trains(models.Model):
    train_code = models.CharField('Код поезда', max_length=20, unique=True)
    train_start = models.ForeignKey(Cities, related_name="Место_старта", on_delete=models.CASCADE)
    train_end = models.ForeignKey(Cities, related_name='Конечная_остановка', on_delete=models.CASCADE)
    trip_time = models.IntegerField('Время в пути')


class Routes(models.Model):
    route_name = models.CharField('имя маршрута', max_length=30)
    route_start = models.ForeignKey(Cities, related_name='Начало_маршрута', on_delete=models.CASCADE)
    route_end = models.ForeignKey(Cities, related_name='Конец_маршрута', on_delete=models.CASCADE)
