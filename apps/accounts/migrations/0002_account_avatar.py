# Generated by Django 4.2.4 on 2023-09-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='static/placeholder.png', upload_to='static/avatars'),
        ),
    ]
