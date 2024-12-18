# Generated by Django 5.1.3 on 2024-11-25 14:17

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edit', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('url', models.URLField(blank=True, default='', max_length=255, null=True)),
                ('details', models.TextField(blank=True, default='', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
