# Generated by Django 2.0.1 on 2018-04-12 13:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signal',
            old_name='channel',
            new_name='encryption_type',
        ),
        migrations.RenameField(
            model_name='signal',
            old_name='encryption',
            new_name='meter_distance',
        ),
        migrations.RenameField(
            model_name='signal',
            old_name='modulation',
            new_name='modulation_id',
        ),
        migrations.RemoveField(
            model_name='signal',
            name='bssid',
        ),
        migrations.RemoveField(
            model_name='signal',
            name='essid',
        ),
        migrations.AddField(
            model_name='encryption',
            name='key_size',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensor',
            name='encryption_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensor',
            name='modulation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensor',
            name='sensor_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensor',
            name='ssid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='signal',
            name='azimuth',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='signal',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='signal',
            name='sample_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rf.Sensor'),
        ),
        migrations.AddField(
            model_name='signal',
            name='sensor_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='signal',
            name='sensor_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='signal',
            name='signal_strength',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='encryption',
            name='encryption_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rf.Signal'),
        ),
        migrations.AlterField(
            model_name='modulation',
            name='modulation_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rf.Signal'),
        ),
    ]