# Generated by Django 3.1.2 on 2021-02-18 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20201217_0910'),
        ('store', '0016_auto_20210209_1034'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shopproduct',
            unique_together={('shop', 'product')},
        ),
    ]