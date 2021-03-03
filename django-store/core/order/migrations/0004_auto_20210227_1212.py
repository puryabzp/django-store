# Generated by Django 3.1.2 on 2021-02-27 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20210226_1156'),
        ('order', '0003_auto_20210204_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='shop_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shopproduct', verbose_name='Shop product'),
        ),
    ]