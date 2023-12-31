# Generated by Django 4.2.6 on 2023-10-19 07:27

from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('isbn', models.CharField(error_messages={'unique': 'Ikkita bir xil kitob kiritishning iloji yuq'}, max_length=50, unique=True)),
                ('author', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('is_e', models.BooleanField(default=False)),
                ('file', models.FileField(blank=True, null=True, upload_to=library.models.save_file)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.CharField(default=library.models.tokenize, editable=False, max_length=20)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('scheduled_at', models.DateField()),
                ('is_ended', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]
