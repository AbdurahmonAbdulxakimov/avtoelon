# Generated by Django 3.2 on 2024-02-07 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionvalueextended',
            name='option_value',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='values_extended', to='option.optionvalue'),
            preserve_default=False,
        ),
    ]
