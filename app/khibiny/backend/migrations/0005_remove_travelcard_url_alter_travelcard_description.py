# Generated by Django 4.2.3 on 2023-11-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_travelcard_url_alter_travelcard_season'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelcard',
            name='url',
        ),
        migrations.AlterField(
            model_name='travelcard',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]
