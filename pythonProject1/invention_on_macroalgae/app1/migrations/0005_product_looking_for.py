# Generated by Django 4.0.7 on 2022-12-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_purchase_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_looking_for',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('company_type', models.CharField(max_length=200)),
                ('product', models.CharField(max_length=200)),
                ('licence_number', models.CharField(max_length=200)),
                ('licence_document', models.FileField(null=True, upload_to='')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
