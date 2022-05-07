# Generated by Django 4.0.4 on 2022-05-07 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainBot', '0005_alias_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label_Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('labelName', models.CharField(default='', max_length=50)),
                ('url', models.CharField(default='', max_length=50)),
                ('mdt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Alias_Url',
        ),
    ]