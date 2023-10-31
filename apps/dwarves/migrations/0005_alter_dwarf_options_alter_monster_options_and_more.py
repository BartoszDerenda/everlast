# Generated by Django 4.2.4 on 2023-10-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwarves', '0004_alter_dwarf_agility_multiplier_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dwarf',
            options={'verbose_name': 'Dwarf', 'verbose_name_plural': 'Dwarves'},
        ),
        migrations.AlterModelOptions(
            name='monster',
            options={'verbose_name': 'Monster', 'verbose_name_plural': 'Monsters'},
        ),
        migrations.AddField(
            model_name='monster',
            name='battle_power',
            field=models.IntegerField(default=0),
        ),
    ]