# Generated by Django 2.2.4 on 2024-05-10 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionar_Informacion', '0003_auto_20240509_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='CedulaC',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='Placa',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
