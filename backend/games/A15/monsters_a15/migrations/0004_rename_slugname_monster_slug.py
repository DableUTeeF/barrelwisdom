# Generated by Django 5.0.5 on 2024-06-19 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monsters_a15', '0003_alter_monster_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monster',
            old_name='slugname',
            new_name='slug',
        ),
    ]