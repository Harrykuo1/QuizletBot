# Generated by Django 4.0.4 on 2022-05-12 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainBot', '0008_alter_global_label_url_url_alter_label_url_labelname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='global_label_url',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='label_url',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
    ]