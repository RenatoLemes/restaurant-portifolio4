# Generated by Django 4.2.4 on 2023-08-24 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.CharField(max_length=10)),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('guest_name', models.CharField(max_length=100)),
                ('guest_count', models.PositiveIntegerField()),
                ('canceled', models.BooleanField(default=False)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.table')),
            ],
        ),
    ]
