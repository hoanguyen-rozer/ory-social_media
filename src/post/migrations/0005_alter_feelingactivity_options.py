# Generated by Django 4.0.4 on 2022-04-29 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_feelinguser_post_alter_feelinguser_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feelingactivity',
            options={'verbose_name': 'feeling/activity', 'verbose_name_plural': 'feeling/activities'},
        ),
    ]