# Generated by Django 2.0.2 on 2018-04-14 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historydata',
            name='Doctor_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='catalog.Doctor'),
        ),
    ]
