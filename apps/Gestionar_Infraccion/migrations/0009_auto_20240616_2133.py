# Generated by Django 2.2.4 on 2024-06-17 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionar_Infraccion', '0008_auto_20240616_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infraccion_transito',
            name='NumeroInfraccion',
            field=models.CharField(max_length=1000000, primary_key=True, serialize=False),
        ),
    ]
