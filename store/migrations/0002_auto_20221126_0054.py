# Generated by Django 3.1 on 2022-11-25 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slud',
            new_name='slug',
        ),
    ]