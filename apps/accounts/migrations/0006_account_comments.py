# Generated by Django 4.2.4 on 2023-10-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_profile_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='comments',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
