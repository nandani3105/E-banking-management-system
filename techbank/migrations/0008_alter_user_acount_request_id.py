# Generated by Django 5.0.6 on 2025-06-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbank', '0007_rename_account_user_acount_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_acount_request',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
