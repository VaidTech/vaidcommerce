# Generated by Django 3.0.1 on 2020-05-18 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ordered',
            new_name='order_verify',
        ),
    ]
