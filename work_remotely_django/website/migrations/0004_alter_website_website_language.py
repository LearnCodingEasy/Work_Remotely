# Generated by Django 5.1.3 on 2024-11-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_website_website_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='website_language',
            field=models.CharField(choices=[('arabic', 'Arabic'), ('english', 'English')], default='english', max_length=25),
        ),
    ]
