# Generated by Django 3.0 on 2020-01-12 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
    ]