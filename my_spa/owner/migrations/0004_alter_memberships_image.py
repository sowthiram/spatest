# Generated by Django 4.1.4 on 2022-12-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_alter_memberships_desc_alter_memberships_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberships',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
