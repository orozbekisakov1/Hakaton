# Generated by Django 4.0.4 on 2022-05-15 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
