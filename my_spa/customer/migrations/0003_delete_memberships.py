# Generated by Django 4.1.2 on 2022-12-12 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_memberships_delete_membership'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Memberships',
        ),
    ]
