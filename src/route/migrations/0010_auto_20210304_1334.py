# Generated by Django 3.1.7 on 2021-03-04 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0009_auto_20210226_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='train_end',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='train_end_set', to='route.cities', verbose_name='Конечная остановка'),
        ),
        migrations.AlterField(
            model_name='trains',
            name='train_start',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='train_start_set', to='route.cities', verbose_name='Место старта'),
        ),
        migrations.AlterField(
            model_name='trains',
            name='trip_time',
            field=models.PositiveIntegerField(verbose_name='Время в пути'),
        ),
    ]
