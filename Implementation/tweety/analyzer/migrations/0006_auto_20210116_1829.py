# Generated by Django 2.2.12 on 2021-01-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0005_auto_20210116_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetsummary',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
