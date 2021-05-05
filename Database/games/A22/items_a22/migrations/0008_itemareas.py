# Generated by Django 3.0.6 on 2021-05-02 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations_a22', '0003_location_isdlc'),
        ('items_a22', '0007_auto_20210502_0417'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations_a22.Location')),
                ('gatherdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items_a22.ItemLocations')),
            ],
        ),
    ]
