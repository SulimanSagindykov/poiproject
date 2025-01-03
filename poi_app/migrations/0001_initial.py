# Generated by Django 5.1.3 on 2024-11-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('category', models.CharField(choices=[('restaurant', 'Restaurant'), ('mosque', 'Mosque'), ('fitness club', 'Fitness club'), ('cafe', 'Cafe'), ('hotel', 'Hotel'), ('medical', 'Medical'), ('hijama center', 'Hijama center')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
