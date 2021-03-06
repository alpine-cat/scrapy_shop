# Generated by Django 3.0 on 2020-01-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_url', models.CharField(max_length=256)),
                ('category', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('price', models.CharField(max_length=16)),
                ('images', models.TextField()),
                ('sizes', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
