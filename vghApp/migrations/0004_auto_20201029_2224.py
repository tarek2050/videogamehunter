# Generated by Django 3.1.2 on 2020-10-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vghApp', '0003_auto_20201029_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Prix1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Prix2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
