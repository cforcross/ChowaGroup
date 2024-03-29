# Generated by Django 3.1 on 2021-06-20 13:41

from django.db import migrations, models
import src.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=200, unique=True, validators=[src.validators.email_validator]),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=50, validators=[src.validators.bleach_validator]),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=50, validators=[src.validators.bleach_validator]),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=50, validators=[src.validators.bleach_validator]),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[src.validators.bleach_validator]),
        ),
    ]
