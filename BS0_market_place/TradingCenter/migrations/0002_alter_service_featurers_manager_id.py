# Generated by Django 3.2.5 on 2021-08-05 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TradingCenter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_featurers',
            name='manager_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TradingCenter.services_manager'),
        ),
    ]
