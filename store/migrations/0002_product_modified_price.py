# Generated by Django 3.1.7 on 2024-04-14 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='modified_price',
            field=models.IntegerField(default=True),
        ),
    ]
