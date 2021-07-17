# Generated by Django 3.2.4 on 2021-07-17 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('route', models.TextField(blank=True, null=True)),
                ('side_effects', models.TextField(blank=True, null=True)),
                ('before_care', models.TextField(blank=True, null=True)),
                ('after_care', models.TextField(blank=True, null=True)),
                ('protect_against', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('first_day_from_birth', models.PositiveIntegerField()),
                ('last_day_from_birth', models.PositiveIntegerField()),
                ('booster', models.BooleanField(default=False)),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccine.vaccine')),
            ],
        ),
    ]