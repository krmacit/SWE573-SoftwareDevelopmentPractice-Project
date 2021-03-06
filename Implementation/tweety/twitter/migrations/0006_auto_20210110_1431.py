# Generated by Django 2.2.12 on 2021-01-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_auto_20210110_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='contextannotation',
            name='domain_description',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contextannotation',
            name='domain_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contextannotation',
            name='entity_description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contextannotation',
            name='entity_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contextannotation',
            name='domain_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='contextannotation',
            name='entity_id',
            field=models.BigIntegerField(),
        ),
        migrations.DeleteModel(
            name='ContextAnnotationDomain',
        ),
        migrations.DeleteModel(
            name='ContextAnnotationEntity',
        ),
    ]
