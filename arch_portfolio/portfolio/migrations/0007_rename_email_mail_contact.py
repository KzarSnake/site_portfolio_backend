# Generated by Django 3.2.23 on 2024-02-02 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_rename_contact_mail_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mail',
            old_name='email',
            new_name='contact',
        ),
    ]
