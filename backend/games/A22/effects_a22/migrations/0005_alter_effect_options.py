# Generated by Django 3.2.9 on 2021-12-12 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('effects_a22', '0004_auto_20210829_2330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='effect',
            options={'ordering': ['index']},
        ),
    ]