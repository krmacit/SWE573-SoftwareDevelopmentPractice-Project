# Generated by Django 2.2.12 on 2021-01-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0007_auto_20210116_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='finaltableall',
            name='tweet_count',
            field=models.IntegerField(default=0),
        ),
    ]
