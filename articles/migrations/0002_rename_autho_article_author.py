# Generated by Django 5.0.9 on 2024-10-17 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='autho',
            new_name='author',
        ),
    ]
