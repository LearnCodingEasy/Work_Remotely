# Generated by Django 5.1.3 on 2024-11-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='website_type',
            field=models.CharField(choices=[('services', 'Services'), ('templates', 'Templates'), ('employment', 'Employment')], default='services', max_length=25),
        ),
    ]