# Generated by Django 3.2.9 on 2021-12-21 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERVIEW', '0010_alter_resources_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='image',
            field=models.ImageField(default='', upload_to='hello/'),
        ),
    ]