# Generated by Django 2.0.2 on 2018-03-25 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potentialmatch',
            name='gid',
            field=models.ForeignKey(db_column='gid', on_delete=django.db.models.deletion.CASCADE, to='app_basic.Group'),
        ),
        migrations.AlterField(
            model_name='potentialmatch',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to='app_basic.AdvancedUser'),
        ),
    ]
