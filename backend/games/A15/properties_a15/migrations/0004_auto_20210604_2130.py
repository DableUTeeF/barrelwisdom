# Generated by Django 3.0.6 on 2021-06-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties_a15', '0003_auto_20210604_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]