# Generated by Django 2.1.7 on 2019-03-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.CharField(max_length=15)),
                ('time_zone', models.CharField(max_length=255)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('region', models.CharField(max_length=255)),
                ('region_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country_name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=255)),
                ('country_code3', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=10)),
                ('dma_code', models.PositiveIntegerField(default=0)),
                ('area_code', models.PositiveIntegerField(default=0)),
                ('metro_code', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
