# Generated by Django 4.0.1 on 2022-02-08 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='accepted_at',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='is_accepted',
        ),
        migrations.AddField(
            model_name='friend',
            name='is_accept',
            field=models.BooleanField(default=False, verbose_name='is accept'),
        ),
    ]
