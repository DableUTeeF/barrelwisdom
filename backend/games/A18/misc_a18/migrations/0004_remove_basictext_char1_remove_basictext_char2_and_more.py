# Generated by Django 4.1.4 on 2023-03-02 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misc_a18', '0003_basictext_char1_basictext_char2_basictext_char3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basictext',
            name='char1',
        ),
        migrations.RemoveField(
            model_name='basictext',
            name='char2',
        ),
        migrations.RemoveField(
            model_name='basictext',
            name='char3',
        ),
        migrations.RemoveField(
            model_name='basictext',
            name='char4',
        ),
    ]
