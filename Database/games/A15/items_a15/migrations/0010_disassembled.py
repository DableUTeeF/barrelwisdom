# Generated by Django 3.0.6 on 2021-06-07 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_a15', '0009_auto_20210607_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disassembled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items_a15.Item')),
                ('parent', models.ManyToManyField(related_name='disassembledparent', to='items_a15.Item')),
            ],
        ),
    ]
