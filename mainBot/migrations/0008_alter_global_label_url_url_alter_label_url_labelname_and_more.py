# Generated by Django 4.0.4 on 2022-05-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainBot', '0007_global_label_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='global_label_url',
            name='url',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='label_url',
            name='labelName',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='label_url',
            name='url',
            field=models.CharField(default='', max_length=120),
        ),
    ]
