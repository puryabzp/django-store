# Generated by Django 3.1.2 on 2020-12-31 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_basket_basketitems_like_order_orderitems_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='condition',
            field=models.BooleanField(default=True, verbose_name='Condition'),
        ),
    ]
