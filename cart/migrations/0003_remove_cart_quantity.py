# Generated by Django 4.2.6 on 2023-10-23 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
