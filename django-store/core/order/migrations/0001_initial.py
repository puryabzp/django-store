# Generated by Django 3.1.2 on 2021-01-07 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0011_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_baskets', related_query_name='user_baskets', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Basket',
                'verbose_name_plural': 'Baskets',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', related_query_name='user_order', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='amount')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Count')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', related_query_name='order_item', to='order.order', verbose_name='Order')),
                ('shop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shopproduct', verbose_name='Order Item')),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Count')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_item', related_query_name='basket_item', to='order.basket', verbose_name='Basket')),
                ('shop_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shopproduct', verbose_name='Shop product')),
            ],
        ),
    ]