# Generated by Django 4.0.4 on 2022-05-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainBot', '0004_alter_license_key_licensekey_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alias_Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('aliasName', models.CharField(default='', max_length=50)),
                ('url', models.CharField(default='', max_length=50)),
                ('mdt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
