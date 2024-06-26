# Generated by Django 5.0.4 on 2024-04-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juhaerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinglog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('duration', models.PositiveBigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
