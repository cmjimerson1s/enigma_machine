# Generated by Django 3.2.18 on 2023-05-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contactus_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone_number',
            field=models.CharField(max_length=14),
        ),
    ]