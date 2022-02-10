# Generated by Django 4.0.1 on 2022-01-20 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('USERVIEW', '0013_resorucerelatedlinks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resorucerelatedlinks',
            name='id',
        ),
        migrations.AddField(
            model_name='resorucerelatedlinks',
            name='heading',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='resorucerelatedlinks',
            name='link_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='resorucerelatedlinks',
            name='resoruce_id',
            field=models.ForeignKey(db_column='resoruce_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='USERVIEW.resources'),
        ),
        migrations.AddField(
            model_name='resorucerelatedlinks',
            name='url',
            field=models.CharField(default='', max_length=400),
        ),
    ]