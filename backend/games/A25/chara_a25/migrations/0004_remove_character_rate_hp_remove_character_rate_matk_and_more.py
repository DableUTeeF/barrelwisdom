# Generated by Django 4.2.5 on 2023-10-14 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chara_a25', '0003_alter_skill_options_skill_index_alter_skill_val2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='rate_hp',
        ),
        migrations.RemoveField(
            model_name='character',
            name='rate_matk',
        ),
        migrations.RemoveField(
            model_name='character',
            name='rate_mdfn',
        ),
        migrations.RemoveField(
            model_name='character',
            name='rate_patk',
        ),
        migrations.RemoveField(
            model_name='character',
            name='rate_pdfn',
        ),
    ]