# Generated by Django 3.0.6 on 2020-10-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeHouse', '0002_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='day',
            field=models.TextField(max_length=20, null=True),
        ),
    ]