# Generated by Django 2.2.12 on 2021-01-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0014_auto_20210124_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finaltable',
            name='semantic_compound',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=6, null=True),
        ),
    ]
