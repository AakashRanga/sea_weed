# Generated by Django 4.0.7 on 2022-12-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_specific_product_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specific_product',
            name='solution',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
