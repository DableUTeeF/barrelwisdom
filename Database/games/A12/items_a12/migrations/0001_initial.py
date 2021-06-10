# Generated by Django 3.0.6 on 2021-06-09 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('traits_a12', '0001_initial'),
        ('effects_a12', '0001_initial'),
        ('regions_a12', '0002_region_parent'),
        ('categories_a12', '0001_initial'),
        ('monsters_a12', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item_en',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Item_ja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slugname', models.SlugField(unique=True)),
                ('index', models.IntegerField()),
                ('level', models.IntegerField()),
                ('note', models.CharField(max_length=400)),
                ('isDX', models.BooleanField(default=False)),
                ('isDLC', models.BooleanField(default=False)),
                ('time', models.IntegerField(blank=True, null=True)),
                ('mp', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('uses', models.IntegerField(blank=True, null=True)),
                ('item_type', models.CharField(max_length=15)),
                ('item_subtype', models.CharField(blank=True, max_length=15, null=True)),
                ('categories', models.ManyToManyField(to='categories_a12.Category')),
                ('item_en', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='items_a12.Item_en')),
                ('item_ja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='items_a12.Item_ja')),
                ('locations', models.ManyToManyField(to='regions_a12.Region')),
                ('monsters', models.ManyToManyField(to='monsters_a12.Monster')),
                ('traits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traits_a12.Trait')),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, null=True)),
                ('itemnum', models.IntegerField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredientcat', to='categories_a12.Category')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredientitem', to='items_a12.Item')),
                ('synthitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items_a12.Item')),
            ],
            options={
                'ordering': ['synthitem', 'itemnum'],
            },
        ),
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.IntegerField()),
                ('mp', models.IntegerField()),
                ('lp', models.IntegerField()),
                ('atk', models.IntegerField()),
                ('defen', models.IntegerField()),
                ('spd', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items_a12.Item')),
                ('material', models.ManyToManyField(related_name='equip_materials', to='items_a12.Item')),
            ],
        ),
        migrations.CreateModel(
            name='EffectLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('itemnum', models.IntegerField()),
                ('min_elem', models.IntegerField()),
                ('max_elem', models.IntegerField()),
                ('effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='effects_a12.Effect')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items_a12.Item')),
            ],
            options={
                'ordering': ['itemnum', 'number'],
            },
        ),
        migrations.CreateModel(
            name='CharacterEquip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chars', models.ManyToManyField(to='items_a12.Character')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items_a12.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slugname', models.SlugField(unique=True)),
                ('index', models.IntegerField()),
                ('note', models.CharField(max_length=400)),
                ('isDX', models.BooleanField(default=False)),
                ('isDLC', models.BooleanField(default=False)),
                ('item_en', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='items_a12.Item_en')),
                ('item_ja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='items_a12.Item_ja')),
                ('items', models.ManyToManyField(to='items_a12.Item')),
            ],
            options={
                'ordering': ['index'],
            },
        ),
    ]