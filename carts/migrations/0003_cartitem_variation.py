# Generated by Django 3.1 on 2021-06-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
        ('carts', '0002_auto_20210619_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='Variation',
            field=models.ManyToManyField(to='store.Variation'),
        ),
    ]
