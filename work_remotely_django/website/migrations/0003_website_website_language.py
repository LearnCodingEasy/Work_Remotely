# Generated by Django 5.1.3 on 2024-11-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_website_website_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='website_language',
            field=models.CharField(choices=[('services', 'Arabic'), ('english', 'English')], default='english', max_length=25),
        ),
    ]
