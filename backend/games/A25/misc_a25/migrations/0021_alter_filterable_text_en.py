# Generated by Django 5.0.5 on 2024-07-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc_a25', '0020_alter_name_text_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterable',
            name='text_en',
            field=models.CharField(max_length=40),
        ),
    ]
