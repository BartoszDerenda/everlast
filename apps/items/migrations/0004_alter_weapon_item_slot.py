# Generated by Django 4.2.4 on 2023-11-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_remove_armor_attr_bonus_remove_armor_attr_multi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='item_slot',
            field=models.CharField(default='weapon', max_length=16),
        ),
    ]
