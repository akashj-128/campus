# Generated by Django 3.1 on 2024-01-17 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='country',
            new_name='pincode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address_line_2',
        ),
    ]
