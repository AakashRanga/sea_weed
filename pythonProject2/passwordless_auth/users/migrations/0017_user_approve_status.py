# Generated by Django 4.0.7 on 2023-02-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_user_approve_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_approve',
            name='status',
            field=models.CharField(default='Not Approved', max_length=255),
        ),
    ]