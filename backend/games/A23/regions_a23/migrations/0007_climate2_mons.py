# Generated by Django 4.0.3 on 2022-03-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters_a23', '0006_remove_monster_location'),
        ('regions_a23', '0006_remove_climate_loc_remove_climate_node_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='climate2',
            name='mons',
            field=models.ManyToManyField(to='monsters_a23.monster'),
        ),
    ]