# Generated by Django 4.1.4 on 2023-03-02 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misc_a18', '0004_remove_basictext_char1_remove_basictext_char2_and_more'),
        ('items_a18', '0005_alter_catalyst_action1_alter_catalyst_action2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='char1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='char1', to='misc_a18.character'),
        ),
        migrations.AddField(
            model_name='item',
            name='char2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='char2', to='misc_a18.character'),
        ),
        migrations.AddField(
            model_name='item',
            name='char3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='char3', to='misc_a18.character'),
        ),
        migrations.AddField(
            model_name='item',
            name='char4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='char4', to='misc_a18.character'),
        ),
    ]