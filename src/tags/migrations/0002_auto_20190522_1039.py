# Generated by Django 2.2 on 2019-05-21 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tittle',
            new_name='title',
        ),
    ]