# Generated by Django 3.2.16 on 2022-11-15 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoretable',
            name='grade',
        ),
    ]
