# Generated by Django 4.2 on 2023-04-30 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.ImageField(upload_to='events/images'),
        ),
    ]