# Generated by Django 4.2.6 on 2023-10-19 19:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_token',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]