# Generated by Django 4.1.2 on 2022-10-13 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=20)),
                ('anio', models.IntegerField()),
                ('km', models.IntegerField()),
                ('color', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
