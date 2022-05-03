# Generated by Django 4.0.1 on 2022-02-06 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='FeelingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.feeling')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
