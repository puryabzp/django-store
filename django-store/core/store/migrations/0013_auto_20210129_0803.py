# Generated by Django 3.1.2 on 2021-01-29 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210118_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmeta',
            name='label',
            field=models.CharField(max_length=150, verbose_name='label'),
        ),
    ]
