# Generated by Django 3.2.9 on 2021-12-15 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERVIEW', '0006_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='image',
            field=models.ImageField(upload_to='hello/'),
        ),
        migrations.AlterField(
            model_name='test',
            name='image',
            field=models.FileField(upload_to='hello/'),
        ),
    ]