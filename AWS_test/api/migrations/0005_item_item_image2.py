# Generated by Django 5.0.7 on 2024-08-06 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Item_image2',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
