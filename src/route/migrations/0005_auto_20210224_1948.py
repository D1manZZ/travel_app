# Generated by Django 3.1.7 on 2021-02-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0004_auto_20210224_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='photo',
            field=models.ImageField(default='photos/Moscow.jpg', upload_to='media/photos/'),
        ),
    ]
