# Generated by Django 3.2.4 on 2021-06-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0004_auto_20210610_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='modulos',
            field=models.ManyToManyField(through='administrativo.Matricula', to='administrativo.Modulo'),
        ),
        migrations.AddField(
            model_name='modulo',
            name='estudiantes',
            field=models.ManyToManyField(through='administrativo.Matricula', to='administrativo.Estudiante'),
        ),
    ]