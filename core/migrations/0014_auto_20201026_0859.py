# Generated by Django 2.2.8 on 2020-10-26 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_coupon_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='amount',
            field=models.FloatField(default=20),
        ),
    ]