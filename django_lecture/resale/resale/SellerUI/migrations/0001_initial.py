# Generated by Django 3.0.5 on 2020-04-24 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vmodel', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('age', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('year', models.IntegerField()),
                ('fueltank', models.CharField(choices=[('P', 'Petrol'), ('D', 'Diesel'), ('C', 'CNG')], default='P', max_length=1)),
                ('price', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
