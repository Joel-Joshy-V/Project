# Generated by Django 4.2.6 on 2023-11-04 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_data',
            old_name='mail',
            new_name='email',
        ),
    ]
