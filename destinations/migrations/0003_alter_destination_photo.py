# Generated by Django 4.0.1 on 2022-01-17 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_delete_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='photo',
            field=models.ImageField(upload_to='img/'),
        ),
    ]