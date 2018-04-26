# Generated by Django 2.0.1 on 2018-04-26 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rf', '0004_auto_20180412_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encryption',
            name='encryption_id',
        ),
        migrations.RemoveField(
            model_name='modulation',
            name='modulation_id',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='encryption_type',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='sensor_id',
        ),
        migrations.RemoveField(
            model_name='signal',
            name='encryption_type',
        ),
        migrations.RemoveField(
            model_name='signal',
            name='modulation_id',
        ),
        migrations.AddField(
            model_name='sensor',
            name='encryption',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rf.Encryption'),
        ),
        migrations.AddField(
            model_name='signal',
            name='encryption',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rf.Encryption'),
        ),
        migrations.AddField(
            model_name='signal',
            name='modulation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rf.Modulation'),
        ),
    ]
