# Generated by Django 4.0.7 on 2022-12-26 03:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_specific_product_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specific_product',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
