# Generated by Django 3.2.23 on 2024-02-02 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20240202_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mail',
            old_name='contact',
            new_name='email',
        ),
    ]
