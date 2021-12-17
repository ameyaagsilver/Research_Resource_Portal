# Generated by Django 3.2.9 on 2021-12-16 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('USERVIEW', '0002_auto_20211216_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee_members',
            name='committee_id',
            field=models.ForeignKey(db_column='committee_id', on_delete=django.db.models.deletion.CASCADE, to='USERVIEW.committee'),
        ),
        migrations.AlterField(
            model_name='resource_logbook',
            name='admin_id',
            field=models.ForeignKey(db_column='admin_id', on_delete=django.db.models.deletion.CASCADE, to='USERVIEW.admins'),
        ),
        migrations.AlterField(
            model_name='resource_logbook',
            name='member_id',
            field=models.ForeignKey(db_column='mimber_id', on_delete=django.db.models.deletion.CASCADE, to='USERVIEW.users'),
        ),
        migrations.AlterField(
            model_name='resource_logbook',
            name='resource_id',
            field=models.ForeignKey(db_column='resource_id', on_delete=django.db.models.deletion.CASCADE, to='USERVIEW.resources'),
        ),
        migrations.AlterField(
            model_name='resources',
            name='admin_id',
            field=models.ForeignKey(db_column='admin_id', default='r0Fi0ITEUSMcLPxf2JXUxL3VNK03', on_delete=django.db.models.deletion.CASCADE, to='USERVIEW.admins'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='admin_id',
            field=models.ForeignKey(db_column='admin_id', on_delete=django.db.models.deletion.CASCADE, to='USERVIEW.admins'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='committee_id',
            field=models.ForeignKey(db_column='committee_id', on_delete=django.db.models.deletion.CASCADE, to='USERVIEW.committee'),
        ),
    ]
