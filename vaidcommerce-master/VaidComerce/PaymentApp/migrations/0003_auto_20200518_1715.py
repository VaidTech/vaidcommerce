# Generated by Django 3.0.1 on 2020-05-18 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentApp', '0002_auto_20200518_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='user',
            new_name='user_order',
        ),
    ]
