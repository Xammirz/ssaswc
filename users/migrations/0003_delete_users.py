# Generated by Django 4.2 on 2023-05-30 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
