# Generated by Django 3.2 on 2024-02-07 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0002_optionvalueextended_option_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='is_extended',
        ),
    ]
