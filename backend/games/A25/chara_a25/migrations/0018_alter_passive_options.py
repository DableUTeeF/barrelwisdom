# Generated by Django 5.0.5 on 2024-09-17 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chara_a25', '0017_passive_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passive',
            options={'ordering': ['num']},
        ),
    ]
