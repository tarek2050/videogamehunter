# Generated by Django 3.1.2 on 2020-11-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vghApp', '0007_auto_20201101_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('Img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]