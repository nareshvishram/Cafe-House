# Generated by Django 3.0.6 on 2020-10-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeHouse', '0004_auto_20201022_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='fb',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='instagram',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='linkedIn',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='twitter',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='youtube',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
