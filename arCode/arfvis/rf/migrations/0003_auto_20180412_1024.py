# Generated by Django 2.0.1 on 2018-04-12 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rf', '0002_auto_20180412_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
                ('pictureFileName', models.CharField(max_length=100)),
                ('three_dimensional_Object', models.CharField(max_length=100)),
                ('default_username', models.CharField(max_length=100)),
                ('default_password', models.CharField(max_length=100)),
                ('vendor_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='signal',
            name='apmode',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signal',
            name='bssid',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signal',
            name='essid',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='device_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rf.Signal'),
        ),
    ]