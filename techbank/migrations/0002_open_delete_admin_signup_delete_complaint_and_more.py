# Generated by Django 5.0.6 on 2025-06-01 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techbank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Open',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('choose', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin_signup',
        ),
        migrations.DeleteModel(
            name='complaint',
        ),
        migrations.DeleteModel(
            name='SignUp1',
        ),
        migrations.DeleteModel(
            name='trans',
        ),
    ]
