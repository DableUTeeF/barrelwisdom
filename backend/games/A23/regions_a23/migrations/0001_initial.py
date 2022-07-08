# Generated by Django 4.0.2 on 2022-03-02 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=30)),
                ('reg_en', models.CharField(max_length=30)),
                ('reg_ja', models.CharField(max_length=30)),
                ('reg_ko', models.CharField(max_length=30)),
                ('reg_sc', models.CharField(max_length=30)),
                ('reg_tc', models.CharField(max_length=30)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='regions_a23.region')),
            ],
        ),
    ]