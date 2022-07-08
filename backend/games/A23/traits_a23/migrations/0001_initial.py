# Generated by Django 4.0.2 on 2022-03-01 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trait_en',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Trait_ja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Trait_ko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Trait_sc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Trait_tc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('index', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('trans_atk', models.BooleanField(default=False)),
                ('trans_heal', models.BooleanField(default=False)),
                ('trans_dbf', models.BooleanField(default=False)),
                ('trans_buff', models.BooleanField(default=False)),
                ('trans_wpn', models.BooleanField(default=False)),
                ('trans_arm', models.BooleanField(default=False)),
                ('trans_acc', models.BooleanField(default=False)),
                ('trans_tal', models.BooleanField(default=False)),
                ('trans_syn', models.BooleanField(default=False)),
                ('trans_exp', models.BooleanField(default=False)),
                ('combo1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='traits_a23.trait')),
                ('combo2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='combo_2', to='traits_a23.trait')),
                ('trait_en', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='traits_a23.trait_en')),
                ('trait_ja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='traits_a23.trait_ja')),
                ('trait_ko', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='traits_a23.trait_ko')),
                ('trait_sc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='traits_a23.trait_sc')),
                ('trait_tc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='traits_a23.trait_tc')),
            ],
            options={
                'ordering': ['index'],
            },
        ),
    ]