# Generated by Django 3.2.6 on 2021-08-30 12:25

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_carro_montadora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='montadora',
            field=models.ForeignKey(on_delete=models.SET(core.models.set_default_montadora), to='core.montadora'),
        ),
    ]
