# Generated by Django 4.2.2 on 2023-06-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0006_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
