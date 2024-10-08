# Generated by Django 3.2.7 on 2023-07-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=150)),
                ('user_id', models.CharField(max_length=150)),
                ('station_name', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('time_slot', models.CharField(max_length=150)),
                ('charging_slot', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=150)),
                ('complaints', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=150)),
                ('feedbacks', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locations', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=150)),
                ('month', models.CharField(max_length=150)),
                ('slot', models.CharField(max_length=150)),
                ('amount', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('payment_type', models.CharField(max_length=150)),
                ('card_no', models.CharField(max_length=150)),
                ('cvv', models.CharField(max_length=150)),
                ('cardname', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('longitude', models.CharField(max_length=150)),
                ('latitude', models.CharField(max_length=150)),
                ('slot', models.CharField(max_length=150)),
            ],
        ),
    ]
