# Generated by Django 4.2.6 on 2023-10-19 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
