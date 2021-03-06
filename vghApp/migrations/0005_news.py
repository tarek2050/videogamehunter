# Generated by Django 3.1.2 on 2020-10-30 14:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vghApp', '0004_auto_20201029_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('Slug', models.SlugField(unique=True)),
                ('Description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('Img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
