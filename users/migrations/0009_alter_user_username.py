# Generated by Django 4.0.7 on 2023-04-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'user with this username already exists.'}, max_length=130, unique=True),
        ),
    ]