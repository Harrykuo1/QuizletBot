# Generated by Django 4.0.4 on 2022-05-06 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainBot', '0002_license_key_remove_user_info_studentid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license_key',
            old_name='key',
            new_name='licenseKey',
        ),
    ]
