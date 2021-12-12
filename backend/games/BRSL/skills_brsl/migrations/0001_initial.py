# Generated by Django 3.2.9 on 2021-12-04 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fragments_brsl', '0004_auto_20211124_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill_en',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Skill_ja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Skill_sc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Skill_tc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slugname', models.SlugField(unique=True)),
                ('level', models.CharField(blank=True, max_length=3, null=True)),
                ('ether', models.IntegerField()),
                ('ether_rec', models.IntegerField()),
                ('knockback', models.IntegerField()),
                ('attTag0', models.CharField(blank=True, max_length=50, null=True)),
                ('actTag0', models.CharField(blank=True, max_length=50, null=True)),
                ('min_1_0', models.CharField(blank=True, max_length=50, null=True)),
                ('max_1_0', models.CharField(blank=True, max_length=50, null=True)),
                ('min_2_0', models.CharField(blank=True, max_length=50, null=True)),
                ('max_2_0', models.CharField(blank=True, max_length=50, null=True)),
                ('attTag1', models.CharField(blank=True, max_length=50, null=True)),
                ('actTag1', models.CharField(blank=True, max_length=50, null=True)),
                ('min_1_1', models.CharField(blank=True, max_length=50, null=True)),
                ('max_1_1', models.CharField(blank=True, max_length=50, null=True)),
                ('min_2_1', models.CharField(blank=True, max_length=50, null=True)),
                ('max_2_1', models.CharField(blank=True, max_length=50, null=True)),
                ('character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fragments_brsl.character')),
                ('skill_en', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='skills_brsl.skill_en')),
                ('skill_ja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='skills_brsl.skill_ja')),
                ('skill_sc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='skills_brsl.skill_sc')),
                ('skill_tc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='skills_brsl.skill_tc')),
            ],
        ),
    ]