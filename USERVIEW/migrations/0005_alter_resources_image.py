# Generated by Django 3.2.9 on 2021-12-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERVIEW', '0004_alter_resources_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='image',
            field=models.ImageField(upload_to='h/'),
        ),
    ]