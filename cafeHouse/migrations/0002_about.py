# Generated by Django 3.0.6 on 2020-10-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeHouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]