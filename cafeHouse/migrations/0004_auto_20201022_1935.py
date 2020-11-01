# Generated by Django 3.0.6 on 2020-10-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeHouse', '0003_item_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.TextField(max_length=500, null=True)),
                ('fb', models.TextField(max_length=10, null=True)),
                ('instagram', models.TextField(max_length=10, null=True)),
                ('twitter', models.TextField(max_length=10, null=True)),
                ('youtube', models.TextField(max_length=10, null=True)),
                ('linkedIn', models.TextField(max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='day',
            field=models.IntegerField(null=True),
        ),
    ]
