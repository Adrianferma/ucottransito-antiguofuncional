# Generated by Django 2.2.4 on 2024-07-10 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionar_Infraccion', '0016_auto_20240710_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contadorinfraccion',
            name='CedulaAgente',
            field=models.IntegerField(verbose_name='Cédula del Agente'),
        ),
        migrations.AlterField(
            model_name='contadorinfraccion',
            name='CodigoAgente',
            field=models.IntegerField(verbose_name='Código del Agente'),
        ),
        migrations.AlterField(
            model_name='contadorinfraccion',
            name='ContadorAgente',
            field=models.IntegerField(verbose_name='Contador del Agente'),
        ),
    ]
