# Generated by Django 3.1 on 2021-06-21 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20210620_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Variation',
            new_name='variation',
        ),
    ]
