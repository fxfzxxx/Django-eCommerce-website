# Generated by Django 2.2.8 on 2020-10-31 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='Default',
            new_name='default',
        ),
    ]
