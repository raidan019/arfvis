# Generated by Django 2.0.1 on 2018-04-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rf', '0005_auto_20180426_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
        ),
    ]
