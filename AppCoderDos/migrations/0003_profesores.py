# Generated by Django 4.2.4 on 2023-09-01 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoderDos', '0002_estudiantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('enseñanza', models.CharField(max_length=50)),
            ],
        ),
    ]
