# Generated by Django 4.1.5 on 2023-01-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec_app', '0002_receipes_delete_receipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipes',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]