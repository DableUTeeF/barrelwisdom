# Generated by Django 5.0.7 on 2024-09-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chara_a25', '0021_emblem_eid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['role', '-rarity', '-date', 'slug']},
        ),
        migrations.AlterModelOptions(
            name='memoria',
            options={'ordering': ['-date', '-rarity']},
        ),
        migrations.AddField(
            model_name='character',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='memoria',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
