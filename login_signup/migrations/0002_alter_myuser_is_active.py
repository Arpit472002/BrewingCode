# Generated by Django 4.0 on 2021-12-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]