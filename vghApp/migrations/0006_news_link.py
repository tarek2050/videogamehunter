# Generated by Django 3.1.2 on 2020-10-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vghApp', '0005_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
