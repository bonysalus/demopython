# Generated by Django 3.2.4 on 2021-06-17 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='pname',
        ),
    ]
