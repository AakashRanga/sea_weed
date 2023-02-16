# Generated by Django 4.0.7 on 2022-12-26 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_alter_specific_product_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='pay_slip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=255)),
                ('product', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('boolean', models.BooleanField(default=False)),
            ],
        ),
    ]