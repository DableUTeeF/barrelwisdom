# Generated by Django 4.2.5 on 2023-10-15 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_a25', '0005_alter_recipe_options_remove_combatitem_traits_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
