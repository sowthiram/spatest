# Generated by Django 4.1.2 on 2022-12-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_delete_memberships'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslots',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('booked', 'booked')], default='available', max_length=100),
        ),
    ]
