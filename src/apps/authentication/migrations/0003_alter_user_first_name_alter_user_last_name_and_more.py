# Generated by Django 4.1.3 on 2022-12-18 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_alter_user_first_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=30),
        ),
    ]
