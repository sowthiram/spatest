# Generated by Django 4.1.4 on 2022-12-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_giftcards'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautician',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]