# Generated by Django 4.1.7 on 2023-03-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_remove_client_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]