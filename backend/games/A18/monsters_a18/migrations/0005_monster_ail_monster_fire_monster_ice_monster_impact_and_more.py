# Generated by Django 4.1.7 on 2023-03-05 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters_a18', '0004_alter_monster_options_monster_atk_monster_cole_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='ail',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='monster',
            name='fire',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='monster',
            name='ice',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='monster',
            name='impact',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='monster',
            name='light',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='monster',
            name='magic',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='monster',
            name='pierce',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='monster',
            name='slash',
            field=models.IntegerField(default=1),
        ),
    ]