# Generated by Django 2.0.5 on 2018-05-07 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rf', '0006_imagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='antenna_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='modulation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rf.Modulation'),
        ),
    ]
