# Generated by Django 3.0.8 on 2020-07-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0012_auto_20200721_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.SmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='birthday',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
