# Generated by Django 4.2.5 on 2023-10-15 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc_a25', '0008_trait_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]