# Generated by Django 4.0.3 on 2022-06-30 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_account', '0002_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.IntegerField(choices=[(0, '@moderator'), (1, 'Like'), (2, 'Comment'), (3, 'Reply')], verbose_name='Тип'),
        ),
    ]
