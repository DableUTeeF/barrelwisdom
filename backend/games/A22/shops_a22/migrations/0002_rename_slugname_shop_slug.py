# Generated by Django 5.0.5 on 2024-06-19 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops_a22', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='slugname',
            new_name='slug',
        ),
    ]