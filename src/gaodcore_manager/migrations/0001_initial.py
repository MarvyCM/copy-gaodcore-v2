# Generated by Django 3.1.7 on 2021-04-14 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ConnectorConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('uri', models.TextField(unique=True)),
                ('enabled', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('enabled', models.BooleanField()),
                ('object_location', models.CharField(max_length=255, null=True)),
                ('object_location_schema', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('connector_config',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaodcore_manager.connectorconfig')),
            ],
        ),
        # migrations.RunSQL('ALTER SEQUENCE resource_id_seq RESTART WITH 1000')
    ]
