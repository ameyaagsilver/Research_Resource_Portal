# Generated by Django 3.2.9 on 2021-12-12 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='admins',
        ),
        migrations.DeleteModel(
            name='committee',
        ),
        migrations.DeleteModel(
            name='committee_members',
        ),
        migrations.DeleteModel(
            name='resource_logbook',
        ),
        migrations.DeleteModel(
            name='resources',
        ),
        migrations.DeleteModel(
            name='tender',
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
