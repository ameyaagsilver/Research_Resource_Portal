# Generated by Django 4.0.1 on 2022-02-10 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('USERVIEW', '0025_alter_resourceupdatelogbook_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admins',
            old_name='location',
            new_name='admin_location',
        ),
    ]