# Generated by Django 2.2 on 2019-06-02 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_ordermanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderManager',
        ),
    ]
