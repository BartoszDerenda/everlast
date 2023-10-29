# Generated by Django 4.2.4 on 2023-10-28 19:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_comment_post_date_alter_guestbook_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]