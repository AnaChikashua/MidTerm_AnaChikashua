# Generated by Django 3.1.3 on 2021-12-08 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('flight_id', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('booking_platform', models.CharField(max_length=20)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Booking',
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('country_of_citizenship', models.CharField(max_length=50)),
                ('country_of_residence', models.CharField(max_length=50)),
                ('passport_number', models.CharField(max_length=20)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Passenger',
            },
        ),
        migrations.CreateModel(
            name='FlightManifest',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('booking_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='databases.booking')),
            ],
            options={
                'db_table': 'FlightManifest',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='passenger_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='databases.passenger'),
        ),
        migrations.CreateModel(
            name='BoardingPass',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('qr_code', models.CharField(max_length=65535)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('booking_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='databases.booking')),
            ],
            options={
                'db_table': 'BoardingPass',
            },
        ),
        migrations.CreateModel(
            name='Baggage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('weight_in_k', models.FloatField()),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('booking_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productToProductColors', to='databases.booking')),
            ],
            options={
                'db_table': 'Baggage',
            },
        ),
    ]
