# Generated by Django 4.2.4 on 2023-08-29 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('item_slot', models.CharField(max_length=16)),
                ('rarity', models.CharField(max_length=16)),
                ('tooltip', models.CharField(max_length=255)),
                ('attr_bonus', models.JSONField(default=dict)),
                ('attr_multi', models.JSONField(default=dict)),
                ('armor_values', models.JSONField(default=dict)),
                ('abilities', models.JSONField(blank=True, default=dict, null=True)),
                ('materials', models.JSONField(blank=True, default=dict, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('rarity', models.CharField(max_length=16)),
                ('tooltip', models.CharField(max_length=255)),
                ('materials', models.JSONField(blank=True, default=dict, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('item_slot', models.JSONField(default=list)),
                ('rarity', models.CharField(max_length=16)),
                ('tooltip', models.CharField(max_length=255)),
                ('attr_bonus', models.JSONField(default=dict)),
                ('attr_multi', models.JSONField(default=dict)),
                ('abilities', models.JSONField(blank=True, default=dict, null=True)),
                ('materials', models.JSONField(blank=True, default=dict, null=True)),
            ],
        ),
    ]
