# Generated by Django 5.0.5 on 2024-06-19 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items_br1', '0003_alter_item_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='slugname',
            new_name='slug',
        ),
    ]