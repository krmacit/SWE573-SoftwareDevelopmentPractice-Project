# Generated by Django 2.2.12 on 2021-01-10 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0007_auto_20210110_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contextannotation',
            name='tweet_id',
        ),
    ]
