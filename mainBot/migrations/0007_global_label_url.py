# Generated by Django 4.0.4 on 2022-05-11 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainBot', '0006_label_url_delete_alias_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Global_Label_Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelName', models.CharField(default='', max_length=50)),
                ('url', models.CharField(default='', max_length=50)),
                ('mdt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
